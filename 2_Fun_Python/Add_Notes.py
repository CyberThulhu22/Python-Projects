#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME:           Add_Notes.py
VERSION:        1.0
AUTHOR:         Jesse Leverett (CyberThulhu)
STATUS:         Building Initial code framework
DESCRIPTION:    Allows a User to Add Notes to a '.txt' Document
TO-DO:
USAGE:
COPYRIGHT © 2021 Jesse Leverett
"""
# Imports
import sys
import argparse
import datetime

# Instantiate Parser
PROG_NAME = ''
DESC_TEXT = ''
EPIL_TEXT = ''
parser = argparse.ArgumentParser(prog='', description='Just a simple', epilog='', )

# Add Parser Arguments
OUTP_HELP_TEXT = 'File path to Write/Append Output'
TIME_HELP_TEXT = 'Option to Timestamp Newlines (Default: False)'
parser.add_argument('-o', dest='output', metavar=r'outfile.txt', type=str, help=OUTP_HELP_TEXT)
parser.add_argument('-t', dest='timestamp', default=False, action='store_true', type=bool, help=TIME_HELP_TEXT)

# Parse through created Arguments
pargs = parser.parse_args()


# Defined Functions
def check_file_exists():
    pass

def timestamp_line():
    return "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))

def main():

while True:
    try:
        newlink = input("Enter Website Link: ")

        with open(r"C:\Users\Jesse\OneDrive\Desktop\References_for_SANSSummit_ThreatHunting.txt", "a") as websitelinks:
            websitelinks.writelines(newlink + "\n\r")
                            
    except KeyboardInterrupt:
        break

sys.exit(0)
