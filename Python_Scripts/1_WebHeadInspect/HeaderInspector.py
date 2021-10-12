#!/usr/bin/env python3
"""
NAME: Head-Inspector.py
VERSION: 0.0.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION:
    Takes a provided URL/ List of URLs and Parses through the headers of the Request.
"""
import argparse
from http.server import BaseHTTPRequestHandler
import sys
import json
import requests
import urllib

# Instantiate Argument Parser
parser = argparse.ArgumentParser(description='')
group = parser.add_mutually_exclusive_group(required=True)
# Add Arguments
parser.add_argument('-o', '--output', metavar=r'C:\Outfile.txt', required=False, type=str, help='Outputs the results to a file')
group.add_argument('-u', '--url', metavar='', type=str, help='Provide a URL to GET Headers')
group.add_argument('-uL', '--urlList', metavar='', type=str, help='Provide a list of URLs to GET Headers')

# Parse Through Arguments
args = parser.parse_args()

# Defined Functions
def test_connection(ipaddr, tgtport=80):
    # Test connection to provided URL/URI
    pass

def make_request():
    # Makes request to provided URL/URI
    pass

def read_list(provided_list):
    # If a document is provided as a list, read the provided list and return
    with open(str(provided_list), "r") as open_list:
        read_list = open_list.readlines()
    return read_list

def main():
    pass

# Run Application
if __name__ == "__main__":
    main()
