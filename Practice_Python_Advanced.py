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
def get_apikey():
    return getpass.getpass("API_KEY >")

def test_connection(apikey=args.apikey, ipaddr=args.ipaddr):
    try:
        status_code = request.urlopen(f"https://api.ipgeolocation.io/ipgeo?apiKey={apikey}&ip={ipaddr}").getcode()
        if status_code == 200:
            return status_code
    except error.HTTPError:
        print(f"[-] ERROR (HTTPErr: {error.HTTPError().code})")
        sys.exit(1)
    

if __name__ == "__main__":
    if args.apikey == None: API_KEY = get_apikey()
    else: API_KEY = args.apikey
    print(API_KEY)
    print(test_connection())