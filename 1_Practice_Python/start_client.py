#!/usr/bin/env python3
#-*- Coding: utf-8 -*-
"""
NAME: start_client.py
VERSION: 0.1
AUTHOR: Jesse Leverett (CyberThulhu22)
STATUS: Work In Progress
DESCRIPTION: Client to Connect to Server
TO-DO: Build Initial Code Framework
COPYRIGHT © 2021 Jesse Leverett
"""

# Standard Variables
__author__ = "Jesse Leverett"
__copyright__ = "Copyright (C) 2021 Jesse Leverett"
__license__ = "MIT License"
__version__ = "0.1"

# Imports
import sys
import socket

# DEFINED VARIABLES
TARGET_SERVER = "127.0.0.1"
TARGET_PORT = 60050

# DEFINED CLASS
class StartClient:
    """ Client Object """
    def __init__(self, ip_address:str=TARGET_SERVER, protocol_port:int=TARGET_PORT):
        self.ip_address = ip_address
        self.protocol_port = protocol_port

    def connect_client(self):
        """ Client Connection """
        with socket.socket() as sock:
            sock.connect((self.ip_address, self.protocol_port))
            prepared_msg = "start"
            while prepared_msg.lower() != 'exit':
                prepared_msg = str(input("\nCLIENT>> "))
                encoded_msg = bytes(prepared_msg, "utf-8")
                sock.send(encoded_msg)


def main():
    """ Main Program """
    init_client = StartClient(TARGET_SERVER, TARGET_PORT)
    init_client.connect_client()

if __name__ == "__main__":
    main()
                
