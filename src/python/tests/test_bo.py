from bo import IMAPBO
from unittest.mock import patch, mock_open, MagicMock

class TestIMAPBO():

    def test_on_init(self):
        with patch('imaplib.IMAP4_SSL') as imap4_ssl:
            with patch('imaplib.IMAP4') as imap4:
                bo = IMAPBO()
                bo.server = 'server'
                bo.login = 'login'
                bo.password = 'password'
                bo.on_init()
                imap4_ssl.assert_called_with('server', 993, 10)
                imap4.assert_not_called()