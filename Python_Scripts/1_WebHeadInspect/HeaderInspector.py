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
#import re
import sys
import json
import urllib

# Instantiate Argument Parser
parser = argparse.ArgumentParser(description='', )
urlgroup = parser.add_mutually_exclusive_group(required=True)

# Add Arguments
#parser.add_argument('', '', metavar='', required=True, type=str, default='', help='')
parser.add_argument('-p', '--port', metavar='[port]', required=False, type=int, default=80, help='Allows to select a port if not specified in the URL string')
parser.add_argument('-o', '--output', metavar=r'[C:\Outfile.txt]', required=False, type=str, help='Outputs the results to a file')
urlgroup.add_argument('-u', '--url', metavar='[url]', type=str, help='Provide a URL to GET Headers')
urlgroup.add_argument('-uL', '--urlList', metavar=r'[C:\URL-List.txt]', type=str, help='Provide a list of URLs to GET Headers')


# Parse Through Arguments
args = parser.parse_args()

# Convert URL into usable address
def convert_url(url_uri):
    pass

def test_connection(url_uri):
    # Test connection to provided URL/URI
    status_code = urllib.request.urlopen(url_uri).getcode()
    successful_connect = status_code == 200
    return successful_connect

def get_request(made_req):
    # Makes request to provided URL/URI
    request_dict = dict()
    for header in made_req.header_items():
        jsonl = json.loads(json.dumps(header))
        request_dict[jsonl[0]] = jsonl[1]
    return request_dict

def get_response():
    # Reads the Response from provided URL/URI
    pass

def read_list(provided_list):
    # If a document is provided as a list, read the provided list and return
    with open(str(provided_list), "r") as open_list:
        read_list = open_list.readlines()
    return read_list

def main(url_uri):
    req = urllib.request.Request(str(url_uri))


# Run Application
if __name__ == "__main__":
    while True:
        try:
            main()
            sys.exit(0)
        except KeyboardInterrupt:
            break
    sys.exit(0)
