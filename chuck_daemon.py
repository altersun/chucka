#! /usr/bin/env python3


import daemon
import sys

import chuck_webapp

with daemon.DaemonContext(stdout=sys.stdout):
    chuck_webapp.main()
