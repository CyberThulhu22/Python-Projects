#!/usr/bin/env python3
"""
NAME:
VERSION:
AUTHOR:
DESCRIPTION:
TO-DO:
"""

# Imports
import sys
import argparse
import getpass
from urllib import request, error

# Argparse
parser = argparse.ArgumentParser(description="")
parser.add_argument('-i', "--ipaddr", metavar='abc123', default="8.8.8.8", type=str, help="")
parser.add_argument('-a', "--apikey", metavar='abc123', nargs="?",default=None, type=str, help="")
args = parser.parse_args()

# Getpass


def test_connection(apikey=args.apikey, ipaddr=args.ipaddr):
    try:
        status_code = request.urlopen(f"https://api.ipgeolocation.io/ipgeo?apiKey={apikey}&ip={ipaddr}").getcode()
        if status_code == 200:
            return status_code
    except error.HTTPError as httperr:
        response_data = httperr.read().decode("utf-8", "ignore")
        print(f"[-] ERROR (HTTPErr: {response_data})")
        sys.exit(1)

def get_apikey():
    print("[+] TASK: Please Copy and Paste your API key!")
    return getpass.getpass("[*] API_KEY: ")    

if __name__ == "__main__":
    if args.apikey == None: args.apikey = get_apikey()
    print(args.apikey)
    print(test_connection())