#!/usr/bin/env python3
"""
NAME: IPOwner.py
VERSION: 0.0.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: Gathers IP Info from http://ipinfo.io/ using Token
TO-DO:
    [] Add functionality to IP List; Add Threading to work through List of IPs
    [] Add functionality to Output function to parse response information into CSV/TXT/JSON
"""
import sys
import json
import argparse
import ipaddress
from urllib import request

# Instantiate Argument Parser
description_text = "Outputs IPv4 Information using URL> https://ipinfo.io/"
usage_text = ""
epilog_text = "* You will need to signup/login to ipinfo.io (Free) in order to get a 'Token'\n"
epilog_text += "Note: You will only have 50,000 requests available per month with Free access."

parser = argparse.ArgumentParser(description = f"{description_text}", epilog = f"{epilog_text}",formatter_class=argparse.RawDescriptionHelpFormatter)
ipgroup = parser.add_mutually_exclusive_group(required=True)

# Create Arguments
parser.add_argument('-o', '--output', metavar=r'C:\IP-List.txt', type=str, required=False, help='')
parser.add_argument('-t', '--token', metavar='abcdef0123456789', type=str, required=True, help='')
ipgroup.add_argument('-ip', '--ipaddr', metavar='ipaddr', type=str, help='Provide an IPv4 Address')
ipgroup.add_argument('-ipL', '--iplist', metavar=r'C:\IP-List.txt', type=str, help='Provide a list of IPv4 Address to parse')

# Parse Arguments
args = parser.parse_args()

# Defined Functions
def check_valid_ip_struct(ipaddr=args.ipaddr):
    try:
        ip = ipaddress.ip_address(ipaddr)
    except ValueError:
        return "Address/Netmask is invalid: {}".format(ipaddr)

def test_connection(url_uri):
    # Test connection to provided URL/URI
    status_code = request.urlopen(url_uri).getcode()
    successful_connect = status_code == 200
    return successful_connect

def readFile(file=args.output):
    # Open and Read a File
    outfile = list()
    with open(r'{0}'.format(file), 'r') as infile:
        for line in infile:
            outfile.append(line.rstrip())
    return outfile

def output_results(result_to_outfile, outfile=args.output):
    with open(str(outfile),"a") as output_file:
        output_file.write(result_to_outfile)
    return "Results written to {}".format(output_file)

def ipinfo_build_query(token=args.token, ipaddr=args.ipaddr):
    url = "https://ipinfo.io/{}?token={}".format(ipaddr,token)
    return url

def make_request(req_url):
    print("Making request to {}".format(req_url))
    with request.urlopen(req_url) as req:
        return req.read().decode("utf-8")

if __name__ == "__main__":
    try:
        if test_connection("https://ipinfo.io/") == True:
            check_valid_ip_struct()
            build_url = ipinfo_build_query()
            response_dict = json.loads(make_request(build_url))
            dash = "-" * 40
            print(dash)
            print("{:<12}{:6}".format("HEADER", "DATA"))
            print(dash)
            for i, e in response_dict.items():
                print("{:<12}{:6}".format(i, e))
            sys.exit(0)
        
    except KeyboardInterrupt:
        sys.exit(0)