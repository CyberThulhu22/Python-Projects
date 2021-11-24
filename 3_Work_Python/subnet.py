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

Use: ./subnet.py <ip/cidr>
Alt: ./subnet.py <ip> <mask>
"""

import sys

if __name__=="__main__":
    addr = [0, 0, 0, 0]
    mask = [0, 0, 0, 0]
    cidr = 0
    
    if len(sys.argv) == 2:
        (addr, cidr) = sys.argv[1].split('/')
        
        addr = [int(x) for x in addr.split(".")]
        cidr = int(cidr)
        mask = [( ((1<<32)-1) << (32-cidr) >> i ) & 255 for i in reversed(range(0, 32, 8))]
    elif len(sys.argv) == 3:
        addr = sys.argv[1]
        mask = sys.argv[2]
        
        addr = [int(x) for x in addr.split(".")]
        mask = [int(x) for x in mask.split(".")]
        cidr = sum((bin(x).count('1') for x in mask))
    else:
        print("Use: {0} <ip/cidr>".format(sys.argv[0]))
        print("Alt: {0} <ip> <mask>".format(sys.argv[0]))
        sys.exit(-1)
        
    netw = [addr[i] & mask[i] for i in range(4)]
    bcas = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]
    
    print("Address: {0}".format('.'.join(map(str, addr))))
    print("Mask: {0}".format('.'.join(map(str, mask))))
    print("Cidr: {0}".format(cidr))
    print("Network: {0}".format('.'.join(map(str, netw))))
    print("Broadcast: {0}".format('.'.join(map(str, bcas))))
