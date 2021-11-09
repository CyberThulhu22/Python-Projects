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

def cipher(string, key):
    my_list = []
    for ea in string:
        if ea.islower():
            my_list.append( chr(((ord(ea)+key - ord('a') ) %26) + ord('a') ))
        elif ea.isupper():
            my_list.append( chr(((ord(ea)+key - ord('A'))%26) + ord('A') ))
        else:
            my_list.append(ea)
    return ''.join(my_list)

print(cipher("This is cleartext", 5))
cipher_text = cipher("This is cleartext", 5)

print(cipher(cipher_text, -5))


