#!/usr/bin/env python3

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

    else:
        print("Use: {0} <ip/cidr>".format(sys.argv[0]))
        sys.exit(-1)
        
    netw = [addr[i] & mask[i] for i in range(4)]
        
    print("Address: {0}".format('.'.join(map(str, addr))))
    print("Network: {0}".format('.'.join(map(str, netw))))

https://github.com/CyberThulhu22/Python_Proj/blob/master/Network/IP_Subnet_List/ip_subnet_organizer.py
