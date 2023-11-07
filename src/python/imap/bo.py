import email

from grongier.pex import BusinessOperation
from msg import IMAPRequest, IMAPResponse
from core import IMAPCore

class IMAPBO(BusinessOperation,IMAPCore):

    def on_tear_down(self):
        self._close()

    def on_init(self):
        # set default values
        if not hasattr(self, 'ssl'):
            self.ssl = True

        if not hasattr(self, 'server'):
            raise Exception('server is mandatory')
        
        if not hasattr(self, 'port'):
            if self.ssl:
                self.port = 993
            else:
                self.port = 143

        if not hasattr(self, 'login'):
            raise Exception('login is mandatory')
        
        if not hasattr(self, 'password') and not hasattr(self, 'token'):
            raise Exception('password or token is mandatory')
        
        if not hasattr(self, 'mailbox'):
            self.mailbox = 'INBOX'

        # connect to the server
        if hasattr(self, 'token'):
            self._connect_oauth2(self.server, self.port, self.ssl, self.login, self.token)
        else:
            self._connect(self.server, self.port, self.ssl, self.login, self.password)

        # select the mailbox
        self._select_mailbox(self.mailbox)

    def on_request(self, request: IMAPRequest):
        # search emails
        self._search(request.criteria)

        # fetch emails
        raw_emails = []
        email_messages = []
        for email_id in self.emails:
            raw_email = self._fetch(email_id)
            #raw_emails.append(raw_email)
            email_messages.append(email.message_from_bytes(raw_email))

        # return the response
        return IMAPResponse(email_ids=self.emails, raw_emails=raw_emails, email_messages=email_messages)


