#!/usr/bin/env python3

import argparse as argp

parser = argp.ArgumentParser()
parser.add_argument("-I", "--input", metavar="<input>",
                    action="store_true", type=str, required=False,
                    help="")
args = parser.parse_args()

input_arg = args.input

def readFile(ifile):
    with open(ifile)
