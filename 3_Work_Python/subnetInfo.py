#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME: 
VERSION: 1.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: 
TO-DO:
COPYRIGHT © 2021 Jesse Leverett
"""

#Imports
import sys
import argparse

parser = argparse.ArgumentParser(
    prog = 'subnet_tool',
    formatter_class = argparse.RawDescriptionHelpFormatter,
    description = "Describe tool.",
    epilog = "This is where you put a sentence at the end"
    )
# Setting up arguments
parser.add_argument('ip4file', metavar='<ip list>', type=argparse.FileType('r'), help='File or List of IPv4 address.')
parser.add_argument('--subfile', metavar='<subnet list>', type=argparse.FileType('r'), help='File or List of Subnets.')
parser.add_argument('--outfile', metavar='<out file>', type=argparse.FileType('w'), help='File to output results to.')
args = parser.parse_args()

def readIP(iplist):
    for ea in iplist:
        print(ea)

if __name__=='__main__':
    readIP(args.iplist)
