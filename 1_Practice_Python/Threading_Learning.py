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
import signal
import threading

exit_event = threading.Event()

def signal_handler(signum, frame):
    exit_event.set()

def do_something(seconds:int=1) -> str:
    print(f'Sleeping {seconds} second(s)...\n')
    time.sleep(seconds)
    print(threading.enumerate())

def main():
    start = time.perf_counter()
    t_list = []
    
    for i in range(1, 6):
        t = threading.Thread(target=do_something, args=[i])
        t.start()
        t_list.append(t)
        if exit_event.is_set():
            break
    
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')

if __name__ == "__main__":
    main()
