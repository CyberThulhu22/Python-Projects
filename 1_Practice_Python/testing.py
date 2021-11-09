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

def findmiss(seq):
    seq = sorted(seq)
    print(seq)
    for ea in seq:
        if ea+1 not in seq:
            print( ea + 1)

def fmiss2(seq):
    for e in range(min(seq), max(seq)):
        if e not in seq:
            return e




print(fmiss2([-6,6,5,3,2,-5,-2,1,-1,0,-4,-3]))
