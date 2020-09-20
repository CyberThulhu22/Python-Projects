#!/usr/bin/env python3
"""
"""

## Imported Modules ##
import sys, argparse

## Global Variables ##
ip4List = list()
subList = list()  
addr = [0, 0, 0, 0]
cidr = 0
mask = [( ((1<<32)-1) << (32-cidr) >> i ) & 255 for i in reversed(range(0, 32, 8))]

## Defined Functions ##

## Main Function ##
if __name__=="__main__":
    pass