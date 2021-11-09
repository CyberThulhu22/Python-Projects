#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME: add_note.py
VERSION: 1.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: 
TO-DO:
COPYRIGHT © 2021 Jesse Leverett
"""
# Imports
import sys
import argparse
import datetime

# Instantiate Parser
parser = argparse.ArgumentParser(description='Just a simple')

# Add Parser Arguments
parser.add_argument('-o', '--output', metavar=r'drive:\outfile.txt', type=str, help='Location to send Output')
parser.add_argument('-t', '--timestamp', default=False, action='store_true', type=bool, help='Option to Timestamp each newline (Default: False)')

# Parse through created Arguments
args = parser.parse_args()


# Defined Functions
def check_file_exists():
    pass

def timestamp_line():
    return "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))

while True:
    try:
        newlink = input("Enter Website Link: ")

        with open(r"C:\Users\Jesse\OneDrive\Desktop\References_for_SANSSummit_ThreatHunting.txt", "a") as websitelinks:
            websitelinks.writelines(newlink + "\n\r")
                            
    except KeyboardInterrupt:
        break

sys.exit(0)
