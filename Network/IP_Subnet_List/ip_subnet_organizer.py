#!/usr/bin/env python3
"""
"""
## Imported Modules ##
import sys
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-iL', '--iplist', metavar='<IPv4 List>', required=True, help='Input IPv4 Address List (Each IP needs to be on its own line)')
parser.add_argument('-sL', '--subnetlist', metavar='<Subnet List>', required=True, help='Input Subnet List (Each Subnet IP, needs to be on its own line)')
parser.add_argument('-oF', '--outfile', metavar='<Outfile>', help='Outputs results to a file *Option not implemented yet')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Prints quiet *Option not implemented yet')
group.add_argument('-v', '--v', action='store_true', help='Prints Verbose *Option not implemented yet')
args = parser.parse_args()

## Defined Functions ##
def readFile(file):
    outfile = list()
    with open(r'{0}'.format(file), 'r') as infile:
        for line in infile:
            outfile.append(line.rstrip())
    return outfile

def outFile():
    # Create function to take the output and send to a formated file such as txt.
    pass

def spltIPs(ip):
    return [int(x) for x in ip.split(".")]

def netMask(x = 1):
    netmList = list()
    if x == 1:
        for cidr in range(1, 33):
            netmList.append([( ((1<<32)-1) << (32-cidr) >> i ) & 255 for i in reversed(range(0, 32, 8))])
        return netmList
    elif x == 2:
        return [( ((1<<32)-1) << (32-24) >> i ) & 255 for i in reversed(range(0, 32, 8))]

def netWork(ipaddr, netmask):
    return [ipaddr[i] & netmask[i] for i in range(4)]

def outPut():
    print("SUBNETS \t:\t IPv4s")
    for key, item in sorted(output.items()):
        print(key, "\t:\t", item)

## Main Prog ##
if __name__=="__main__":

    output = dict()
    IPlist = readFile(args.iplist)
    SUBlist = readFile(args.subnetlist)
    
    for ip in IPlist:
        masklist = list()
        counter = 0
        
        for nm in netMask(1):
            masklist.append('.'.join(map(str, netWork(spltIPs(ip), nm))))
        
        while counter != len(SUBlist):
            for sub in SUBlist:
                
                if any(masklist) == sub and sub in output:
                    output.setdefault(sub, [])
                    output[sub].append(ip)
                    counter = len(SUBlist)
                    break
                elif any(masklist) == sub:
                    output.setdefault(sub, [])
                    output[sub].append(ip)
                    counter = len(SUBlist)
                    break
                else:
                    addnew = '.'.join(map(str, netWork(spltIPs(ip), netMask(2))))
                    output.setdefault(addnew,[])
                    output[addnew].append(ip)
                    counter = len(SUBlist)
                    break
    for sub in SUBlist:
        if sub not in output:
            output.setdefault(sub, [])
            output[sub].append('')

    print(outPut())
