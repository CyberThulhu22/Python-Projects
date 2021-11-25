#!/usr/bin/env python3 -tt
#-*- Coding: utf-8 -*-

"""
NAME: _PYTHON_LEARNING_Hello_World.py
VERSION: None
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Complete
DESCRIPTION: Collection Learning Function Building
TO-DO:  N/A
USAGE: ./_PYTHON_LEARNING_Hello_World.py
COPYRIGHT © 2021 Jesse Leverett

You can easily just use the following to say 'Hello, World!':
print("Hello, World!")

But I decided to Be a little Extra to have more of a Code base.
"""

# Initialized Variables
WORLD = "World"

# Initial Functions
def hello_message(text:str=WORLD) -> str:
    """ Simple Function to Print Hello World """
    return f"Hello, {text}!"

# Main Function
def main() -> None:
    """ Main Code """
    try:
        print(hello_message())
    except:
        print("[-] Error! Exiting")
        exit()

# Running the Code
if __name__ == "__main__":
    main()
