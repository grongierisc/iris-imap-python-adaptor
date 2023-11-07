import imaplib
import email

class IMAPCore():

    def _connect(self, server, port, ssl, login, password):
        if ssl:
            self.imap = imaplib.IMAP4_SSL(server, port)
        else:
            self.imap = imaplib.IMAP4(server, port)
        self.imap.login(login, password)

    def _connect_oauth2(self, server, port, ssl, login, oauth2_token):
        if ssl:
            self.imap = imaplib.IMAP4_SSL(server, port)
        else:
            self.imap = imaplib.IMAP4(server, port)
        self.imap.authenticate('XOAUTH2', lambda x: 'user=%s\1auth=Bearer %s\1\1' % (login, oauth2_token))

    def _select_mailbox(self, mailbox):
        self.mailbox = mailbox
        self.imap.select(mailbox)

    def _search(self, criteria):
        typ, data = self.imap.search(None, criteria)
        self.emails = data[0].split()

    def _fetch(self, email_id):
        typ, data = self.imap.fetch(email_id, '(RFC822)')
        return data[0][1]
    
    def _download_attachment(self, email_id, filename):
        typ, data = self.imap.fetch(email_id, '(RFC822)')
        msg = email.message_from_string(data[0][1])
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            if part.get_filename() == filename:
                fp = open(filename, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                return True
        return False
    
    def _close(self):
        self.imap.close()
        self.imap.logout()