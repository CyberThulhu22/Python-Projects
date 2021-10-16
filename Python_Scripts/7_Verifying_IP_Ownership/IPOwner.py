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
import threading
from typing_extensions import Required
from urllib import request, error
from datetime import datetime
import urllib

# Instantiate Argument Parser
desc_text = "Outputs IPv4 Information using URL> https://ipinfo.io/"
epilog_text = "* You will need to signup/login to ipinfo.io (Free) in order to get a 'Token'\n"
epilog_text += "Note: You will only have 50,000 requests available per month with Free access."


argumnt = argparse.ArgumentParser(description= f"{desc_text}", epilog= f"{epilog_text}", formatter_class= argparse.RawDescriptionHelpFormatter)
ipgroup = argumnt.add_mutually_exclusive_group(required=True)
authkey = argumnt.add_mutually_exclusive_group(required=True)

# Create Arguments
output_help_text = ""
ipaddr_help_text = ""
iplist_help_text = ""
tokens_help_text = ""
authky_help_text = ""


argumnt.add_argument('-o', '--output', metavar=r'C:\IP-List.txt', type=str, required=False, help=output_help_text)
ipgroup.add_argument('-i', '--ipaddr', metavar='ipaddr', type=str, help=ipaddr_help_text)
ipgroup.add_argument('-iL','--iplist', metavar=r'C:\IP-List.txt', type=str, help=iplist_help_text)
authkey.add_argument('-t', '--token', metavar='abcdef0123456789', type=str, help=tokens_help_text)
authkey.add_argument('-a', '--authkey', metavar="abcdef0123456789", type=str, help=authky_help_text)

# Parse Arguments
args = argumnt.parse_args()
print(args)

# Defined Class
class IPinfoIO:
    def __init__(self, ipaddr=None, token=None):
        self.ipaddr = ipaddr
        self.token = token
        self.url = "http://ipinfo.io"
    
    def check_valid_ip_struct(self):
        try:
            ip = ipaddress.ip_address(self.ipaddr)
            print("[+] TASK: Gathering Information for Address/Netmask: {}".format(self.ipaddr))
            return True
        except ValueError:
            print("[-] ERROR: Address/Netmask is invalid...Skipping: {}".format(self.ipaddr))
            return False

    def test_connection(self):
            # Test connection to provided URL/URI
            try:
                status_code = request.urlopen(self.url).getcode()
                successful_connect = status_code == 200
                return successful_connect
            except error.URLError:
                print("[-] ERROR (WIN: 10061): No connection could be made because the target machine actively refused it.")
                sys.exit(1)

    def ipinfo_build_query(self):
        built_url = "https://ipinfo.io/{}?token={}".format(self.ipaddr,self.token)
        return built_url

    def make_request(self, req_url):
        print("Making request to {}".format(req_url))
        with request.urlopen(req_url) as req:
            return req.read().decode("utf-8")

# Defined Functions
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


if __name__ == "__main__":
    try:
        start_time = datetime.now()
        if IPinfoIO().test_connection() != True:
            print("[-] ERROR (HTML: 404): Site is not up!")
            sys.exit(0)
        if args.ipaddr != None:
            listed_address = IPinfoIO(args.ipaddr, args.token)
            if listed_address.check_valid_ip_struct():
                pass
        elif args.iplist != None:
            for ipaddr in readFile(args.iplist):
                listed_address = IPinfoIO(ipaddr, args.token)
                if listed_address.check_valid_ip_struct() == True:
                    pass         
        end_time = datetime.now()
        exec_time = end_time - start_time
        print(f"Total execution time for the function {exec_time}")

    except KeyboardInterrupt:
        print("[-] KEY INTERRUPT: Program will now EXIT!")
        sys.exit(0)
    
    # try:
    #     if test_connection("https://ipinfo.io/") == True:
    #         check_valid_ip_struct()
    #         build_url = ipinfo_build_query()
    #         response_dict = json.loads(make_request(build_url))
    #         dash = "-" * 40
    #         print(dash)
    #         print("{:<12}{:6}".format("HEADER", "DATA"))
    #         print(dash)
    #         for i, e in response_dict.items():
    #             print("{:<12}{:6}".format(i, e))
    #         sys.exit(0)
        
    # except KeyboardInterrupt:
    #     sys.exit(0)