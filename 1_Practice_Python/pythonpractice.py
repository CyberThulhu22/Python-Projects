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

# An example of a variable
myvar = "This variable is a string"
numvar = 10 # This is an example number variable

newList = []
spltlst = myvar.split()
for ea in myvar:
    newea = ea.upper()
    newList.append(newea)

anotherList = []
for i in spltlst:
    newi = i.capitalize()
    anotherList.append(newi)

print("".join(newList))
print(" ".join(anotherList))