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

def Chained(functions):
    def chain(input):
        for f in functions:
            input = f(input)
        return input
    return chain

def f1(x):
    return x*2
def f2(x):
    return x+2
def f3(x):
    return x**2

print(Chained([f1,f2,f3])(0))
