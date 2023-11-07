#!/bin/bash

set -m

fg %1

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
iop --init

# load production
iop -m /irisdev/app/src/python/imap/settings.py

# start production
iop --start dc.Python.Production &