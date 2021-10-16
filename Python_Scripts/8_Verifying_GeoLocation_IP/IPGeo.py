#!/usr/bin/env python3
"""
NAME: IPGeo.py
VERSION: 0.0.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: Queries and IP Address or List of IP Addresses for Information from API IPGeolocation IO Website
TO-DO:
"""
import sys
import json
import argparse
import ipaddress
import getpass
from urllib import request, error
from datetime import datetime

# Instantiate Argument Parser
desc_text = "Queries and IP Address or List of IP Addresses for Information from API IPGeolocation IO Website"
epilog_text = "*You will need an API Key from https://api.ipgeolocation.io to run this script\n"
epilog_text += ""

argumnt = argparse.ArgumentParser(description= f"{desc_text}", epilog= f"{epilog_text}", formatter_class= argparse.RawDescriptionHelpFormatter)
ipgroup = argumnt.add_mutually_exclusive_group(required=True)
authkey = argumnt.add_mutually_exclusive_group(required=False)

# Create Arguments
output_help_text = "Enter Path to File that Results will be Recorded to"
ipaddr_help_text = "Enter IP Address"
iplist_help_text = "Enter Path to File containing IP Addresses, each on a new line"
apikey_help_text = "Enter API Key for Batch Mode ONLY (CAUTION: Putting API KEY In-Line could be a Security Concern)"

argumnt.add_argument('-o', '--output', metavar=r'C:\IP-List.txt', type=str, required=False, help=output_help_text)
ipgroup.add_argument('-i', '--ipaddr', metavar='ipaddr', type=str, help=ipaddr_help_text)
ipgroup.add_argument('-iL','--iplist', metavar=r'C:\IP-List.txt', type=str, help=iplist_help_text)
authkey.add_argument('-a', '--apikey', metavar='abc123', nargs="?",default=None, type=str, help=apikey_help_text)

# Parse Arguments
args = argumnt.parse_args()

# Defined Class
class IPGeolocationIO:
    def __init__(self, ipaddr=None, apikey=None):
        self.ipaddr = ipaddr
        self.apikey = apikey
        self.url = "https://api.ipgeolocation.io"
    
    def check_valid_ip_struct(self):
        try:
            ipaddress.ip_address(self.ipaddr)
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
                if successful_connect == True:
                    return "[+] TASK: Website is online! Proceeding..."
                else:
                    print("[-] ERROR (HTML: 404): The website appears to not be up")
                    sys.exit(1)
            except error.URLError:
                print("[-] ERROR (WIN: 10061): No connection could be made because the target machine actively refused it.")
                sys.exit(1)
            except error.HTTPError as httperr:
                response_data = httperr.read().decode("utf-8", "ignore")
                print(f"[-] ERROR (HTTP Error): {response_data}")
                sys.exit(1)
    def get_apikey(self):
        print("[+] TASK: Please Copy and Paste your API key! (Input will be Invisible)")
        return getpass.getpass("   [>] API_KEY: ")

    def build_query(self):
        building_url = "{}/ipgeo?apiKey={}&ip={}".format(self.url, self.apikey, self.ipaddr)
        return building_url

    def make_request(self, req_url):
        print(f"[+] TASK: Making request to https://api.ipgeolocation.io/ipgeo?apiKey=*HIDDEN*&ip={self.ipaddr}")
        try:
            with request.urlopen(req_url) as req:
                return req.read().decode("utf-8")
        except error.HTTPError as httperr:
                response_data = httperr.read().decode("utf-8", "ignore")
                print(f"[-] ERROR (HTTP Error): {response_data}")
                sys.exit(1)


# Defined Functions
def read_file(file=args.iplist):
    # Open and Read a File
    outfile = list()
    with open(r'{0}'.format(file), 'r') as infile:
        for line in infile:
            outfile.append(line.rstrip())
    return outfile

def output_results(result_to_outfile, outfile=args.output):
    # Outputs results to a file or to the screen
    if outfile != None:
        with open(str(outfile),"a") as output_file:
            output_file.write(result_to_outfile)
        return "[!] INFO: Results written to {}".format(output_file)
    else: return result_to_outfile

def json_print(result_data, result_ipaddr=args.ipaddr):
    dash = "-" * 50
    result_header = dash
    result_header += f"\nIP ADDRESS: {result_ipaddr}"
    result_header += "\n{:<25}{:6}\n".format("HEADER", "DATA")
    result_header += dash + "\n"
    for key, value in result_data.items():
        if type(value) == dict:
            res_data = json.dumps(value)
            result_header += "{:<25}{:6}\n".format(key, res_data)
        else: result_header += "{:<25}{:6}\n".format(key, value)
    return result_header


if __name__ == "__main__":

    try:
        start_time = datetime.now()
        IPGeolocationIO().test_connection()
        if args.apikey == None: args.apikey = IPGeolocationIO().get_apikey()
        
        if args.ipaddr != None:
            listed_address = IPGeolocationIO(args.ipaddr, args.apikey)
            if listed_address.check_valid_ip_struct() == True:
                built_url = listed_address.build_query()
                response_data = json.loads(listed_address.make_request(built_url))
                print(output_results(json_print(response_data)))

        elif args.iplist != None:
            for ipaddr in read_file(args.iplist):
                listed_address = IPGeolocationIO(ipaddr, args.apikey)
                if listed_address.check_valid_ip_struct() == True:
                    built_url = listed_address.build_query()
                    response_data = json.loads(listed_address.make_request(built_url))
                    print(output_results(json_print(response_data, ipaddr)))

        end_time = datetime.now()
        exec_time = end_time - start_time
        print(f"[!] INFO: Total execution time for the function {exec_time}")
        sys.exit(0)

    except KeyboardInterrupt:
        print("[-] KEY INTERRUPT: Program will now EXIT!")
        sys.exit(0)