import os
from bo import IMAPBO

CLASSES = {
    'Python.IMAPBO': IMAPBO,
}

server = os.environ.get('server', '')
login = os.environ.get('login', '')
token = os.environ.get('token', '')

PRODUCTIONS = [
    {
        'dc.Python.Production': {
            "@Name": "dc.Demo.Production",
            "@TestingEnabled": "true",
            "@LogGeneralTraceEvents": "false",
            "Description": "",
            "ActorPoolSize": "2",
            "Item": [
                {
                    "@Name": "Python.IMAPBO",
                    "@Category": "",
                    "@ClassName": "Python.IMAPBO",
                    "@PoolSize": "1",
                    "@Enabled": "true",
                    "@Foreground": "false",
                    "@Comment": "",
                    "@LogTraceEvents": "true",
                    "@Schedule": "",
                    "Setting": 
                        {
                            "@Target": "Host",
                            "@Name": "%settings",
                            "#text": "server={server}\nlogin={login}\ntoken={token}".format(server=server, login=login, token=token)
                        }
                }
            ]
        }
    }
]
