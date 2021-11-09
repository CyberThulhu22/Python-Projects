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

import urllib.request
import json
#from flask import jsonify


request_dict = dict()
req = urllib.request.Request('https://bing.com')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    the_response = response.info()

    """for header in response.header_items():
        jsond = json.dumps(header)
        jsonl = json.loads(jsond)
        request_dict[jsonl[0]] = jsonl[1]"""

for header in req.header_items():
    jsonl = json.loads(json.dumps(header))
    request_dict[jsonl[0]] = jsonl[1]


print(request_dict)
print(the_response)
