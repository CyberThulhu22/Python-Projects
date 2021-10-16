#!/usr/bin/env python3
"""
NAME:
VERSION:
AUTHOR:
DESCRIPTION:
TO-DO:
"""

# Imports
import argparse
import getpass

# Argparse
parser = argparse.ArgumentParser(description="")
parser.add_argument('-a', "--apikey", metavar='abc123', nargs="?",default=None, type=str, help="")
args = parser.parse_args()

# Getpass
def get_apikey():
    return getpass.getpass("API_KEY >")

if __name__ == "__main__":
    if args.apikey == None: API_KEY = get_apikey()
    else: API_KEY = args.apikey
    print(API_KEY)