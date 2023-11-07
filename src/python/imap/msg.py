from grongier.pex import Message
from dataclasses import dataclass

@dataclass
class IMAPRequest(Message):
    criteria: str = None
    mailbox: str = None

@dataclass
class IMAPResponse(Message):
    email_ids: list = None
    email_messages: list = None

