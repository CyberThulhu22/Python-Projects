#!/usr/bin/env python3
"""
NAME: IPGeo.py
VERSION: 0.0.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: Find IP Geolocation Information using Abstract API (20,000 Free Lookups)
"""
import argparse

# Instantiate Argument Parser
parser = argparse.ArgumentParser(description='', )
ipgroup = parser.add_mutually_exclusive_group(required=True)

# Add Arguments
#parser.add_argument('', '', metavar='', required=True, type=str, default='', help='')
parser.add_argument('-p', '--port', metavar='[port]', required=False, type=int, default=80, help='Allows to select a port if not specified in the URL string')
parser.add_argument('-o', '--output', metavar=r'[C:\Outfile.txt]', required=False, type=str, help='Outputs the results to a file')
ipgroup.add_argument('-u', '--url', metavar='[url]', type=str, help='Provide a URL to GET Headers')
ipgroup.add_argument('-uL', '--urlList', metavar=r'[C:\URL-List.txt]', type=str, help='Provide a list of URLs to GET Headers')


# Parse Through Arguments
args = parser.parse_args()