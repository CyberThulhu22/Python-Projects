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

import math
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('radius', type=int, metavar='', help='')
parser.add_argument('height', type=int, metavar='', help='')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

if __name__=='__main__':
    print cylinder_volume(args.radius, args.height)
