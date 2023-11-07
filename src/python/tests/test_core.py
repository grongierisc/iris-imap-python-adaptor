import unittest
from imaplib import IMAP4, IMAP4_SSL
from unittest.mock import MagicMock, patch, mock_open
from core import IMAPCore

class TestIMAPCore(unittest.TestCase):
    def setUp(self):
        self.core = IMAPCore()
        self.core.imap = MagicMock()

    def test__connect(self):
        with patch('imaplib.IMAP4_SSL') as imap4_ssl:
            self.core._connect('server', 993, True, 'login', 'password')
            imap4_ssl.assert_called_with('server', 993, 10)
