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
import sys
import datetime
while True:
    try:
        
        newnote = input("Enter Notes: ")
        a = "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))

        with open(r"C:\Users\Jesse\OneDrive\Desktop\WWHF\My_Extras\ConfrenceNotes.txt", "a") as confnotes:
            confnotes.writelines(a + " " + newnote + "\n\r")
                            
    except KeyboardInterrupt:
        break

sys.exit(0)
