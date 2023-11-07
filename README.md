# iris-imap-python-adaptor

This is a simple python script that can be used to connect to an IMAP server and download emails. It is designed to be used with the IRIS email adaptor.

## Installation

### With ZPM

```
zpm "install iris-imap-python-adaptor"
```

Then in a production add this business operation `IRIS.IMAPBO`.

Configure the settings in the `IRIS.IMAPBO` business operation.

```
server=imap.gmail.com
login=xxx@gmail.com
token=ya29.xxx
```

![IRIS.IMAPBO](https://github.com/grongierisc/iris-imap-python-adaptor/blob/master/misc/prod_config.jpg?raw=true)

You can test it with this message :

```
msg.IMAPRequest
{
    "criteria": "(UNSEEN)"
}
```

![IRIS.IMAPBO](https://github.com/grongierisc/iris-imap-python-adaptor/blob/master/misc/test_msg.jpg?raw=true)

result :

```
msg.IMAPResponse
{

    "email_ids": [
        "bytes:MjEzMTc="
    ],
    "raw_emails": [ ],
    "email_messages": [
        {
            "policy": { },
            "_headers": [
                [
                    "Delivered-To",
                    "xxx@gmail.com"
                ],
                [
                    "Received",
                    "by 2002:a98:a901:0:b0:1e6:3d3:6e93 with SMTP id i1csp1439375eie;
                    Sun, 5 Nov 2023 01:12:45 -0800 (PST)"
                ],
                ...
            ],
            ...
        }
    ]
}
```

![IRIS.IMAPBO](https://github.com/grongierisc/iris-imap-python-adaptor/blob/master/misc/result.jpg?raw=true)