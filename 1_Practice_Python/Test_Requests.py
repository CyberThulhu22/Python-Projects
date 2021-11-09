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

import requests
from pprint import pprint as pp
API_KEY = "68692299875344e9b961272cef8b69a6"
IP_LIST = ["131.253.12.5", "131.91.4.55", "192.224.113.15", "199.60.28.111"]

for IP in IP_LIST:
    r = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={IP}")
    print()
    pp(r.json())
