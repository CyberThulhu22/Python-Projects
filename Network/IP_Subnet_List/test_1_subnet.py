#!/usr/bin/env python3
"""
"""
## Imported Modules ##
import sys
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-iL', '--iplist', metavar='<IPv4 List>', required=True, help='Input IPv4 Address List (Each IP needs to be on its own line)')
parser.add_argument('-sL', '--subnetlist', metavar='<Subnet List>', required=True, help='')
parser.add_argument('-oF', '--outfile', metavar='<Outfile>', help='')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Prints quiet')
group.add_argument('-v', '--v', action='store_true', help='Prints Verbose')
args = parser.parse_args()

output = dict()

## Defined Functions ##
def readFile(file):
    outfile = list()
    with open(r'{0}'.format(file), 'r') as infile:
        for line in infile:
            outfile.append(line.rstrip())
    return outfile

def spltIPs(ip):
    return [int(x) for x in ip.split(".")]

def netMask(n=1):
    netmList = list()
    if n == 1:
        for each in range(1, 33):
            netmList.append([( ((1<<32)-1) << (32-each) >> i ) & 255 for i in reversed(range(0, 32, 8))])
        return netmList
    else:
        return netmList.append([( ((1<<32)-1) << (32-each) >> i ) & 255 for i in reversed(range(0, 32, 8))])

def netWork(ipaddr, netmask):
    return [ipaddr[i] & netmask[i] for i in range(4)]

## Main Prog ##
if __name__=="__main__":
    for ipv4 in readFile(args.iplist):
        outputlist = list()
        print("[+] " + ipv4 )
        for nmask in netMask(1):
            outputlist.append('.'.join(map(str, netWork(spltIPs(ipv4), nmask))))
        for subn in readFile(args.subnetlist):
            for each in outputlist:
                if each == subn:
                    print("Subnet Found\t" + each)
                    if each not in output:
                        output.setdefault(subn, [])
                        output[subn].append(ipv4)
                    else:
                        output.setdefault(subn, []).append(ipv4)
                if each != subn:
                    print("Subnet Not Found")
                    if each not in output:
                        #output.setdefault()
                        print()

    print('Subnet\t\t:\t IPv4s')            
    for key, item in output.items():
        print(key, '\t:\t', item)