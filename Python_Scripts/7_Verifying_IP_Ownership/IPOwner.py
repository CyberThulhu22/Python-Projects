#!/usr/bin/env python3
"""
NAME: IPOwner.py
VERSION: 0.0.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION:
"""
import argparse

# Instantiate Argument Parser
parser = argparse.ArgumentParser(description='', )
ipgroup = parser.add_mutually_exclusive_group(required=True)


ipgroup.add_argument('-ip', '--ipaddr', metavar='[ipaddr]', type=str, help='Provide an IPv4 Address')
ipgroup.add_argument('-ipL', '--iplist', metavar=r'[C:\IP-List.txt]', type=str, help='Provide a list of IPv4 Address to parse')