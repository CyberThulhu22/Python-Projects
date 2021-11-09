#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME: 
VERSION: 1.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: 
TO-DO:
COPYRIGHT © 2021 Jesse Leverett
"""

import sys
import time

trials = input("trial: ")
time_out = input("timeout: ")

try:
    for e in range(1,101):
        print(e, (int(trials)%e), e%(int(trials)))
        if e%int(trials) == 0:
            time.sleep(int(time_out))
except KeyboardInterrupt:
    sys.exit(0)
