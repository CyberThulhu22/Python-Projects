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

import time

def do_something(seconds):
    """ DOING SOME SLEEP"""
    print(f"Sleeping {seconds} second(s)...\n")
    time.sleep(seconds)
    return(f"Done Sleeping...{seconds}")

def main():
    """ MAIN PROG """
    start = time.perf_counter()
    do_something()
    do_something()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    
if __name__ == "__main__":
    main()
