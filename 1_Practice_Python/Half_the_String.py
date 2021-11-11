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


Goal: Half the String that is typed; Return first half of a string.

Description:
Make a program that prompts the user to enter a string.
If the string's length is an even number, output exactly half of it.
If it is odd, notify the user that the string is invalid.
"""


#def halfStr():
#    while True:
#        mystr=input("Enter a string:")
#        mthstr=len(mystr) % 2
#        lrng=len(mystr) // 2
#        lst=list(mystr)
#        newl=[]
#        s=''
#        
#        if mthstr == 0:
#            for e in range(0, lrng):
#                newl.append(lst[e])
#            print(s.join(newl))
#            continue
#        else:
#            print("Invalid, try again")
#            continue
#
#halfStr()

#===================================================#
#This is another way to do it:

def first_half(string: str) -> str:
    """Return first half of a string."""
    if len(string) % 2 != 0:
        raise ValueError(f"Ivalid string'{string}' with length {len(string)}")
    else:
        return string[:int(len(string) / 2)]

def second_half(string: str) -> str:
    """Return second half of a string."""
    if len(string) % 2 != 0:
        raise ValueError(f"Ivalid string'{string}' with length {len(string)}")
    else:
        return string[int(len(string) / 2):]

def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        try:
            print("First half:", first_half(string))
            print("Second half:", second_half(string))
        except ValueError as error:
            print(error)
        print("")

if __name__ == "__main__":
    _start_interactively()


