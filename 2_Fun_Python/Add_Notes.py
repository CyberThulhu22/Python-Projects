#!/usr/bin/env python3 -tt
#-*- Coding: utf-8 -*-

"""
NAME:           Add_Notes.py
VERSION:        1.0
AUTHOR:         Jesse Leverett (CyberThulhu)
STATUS:         Building Initial code framework
DESCRIPTION:    Allows a User to Add Notes to a '.txt' Document
TO-DO:
USAGE:          Add_Notes.py [-h] -o <output_file.txt> [-t]
COPYRIGHT © 2021 Jesse Leverett
"""
# Imports
import sys
import argparse
import datetime
from os.path import exists, abspath

# Instantiate Parser
PROG_NAME = "Add_Notes"
DESC_TEXT = "Allows a User to Add Notes to a '.txt' Document"
EPIL_TEXT = "COPYRIGHT © 2021 Jesse Leverett"
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

def timestamp_line() -> str:
    """ Returns Time String """
    return "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))

def main() -> None:
    """ Main Function """
    while True:
        try:
            newline = str(input("Enter Note"))
            with open(pargs.output, "a") as file:
                if pargs.timestamp:
                    file.writelines(timestamp_line() + newline + "\n\r")
                else:
                    file.writelines(newline + "\n\r")
        except KeyboardInterrupt:
            break
    sys.exit(0)

if __name__ == "__main__":
    main()