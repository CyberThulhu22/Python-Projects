#!/usr/bin/env python3
#-*- Coding: utf-8 -*-
"""
NAME: start_server.py
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
import os
import sys
import socket

# DEFINED VARIABLES
HOST_SERVER = "127.0.0.1"
HOST_PORT = 60050

# DEFINED CLASS
class StartServer:
    """ Server Object """
    def __init__(self, ip_address:str=HOST_SERVER, protocol_port:int=HOST_PORT):
        self.ip_address = ip_address
        self.protocol_port = protocol_port

    def handle_client(self, hsock, hipaddr, index):
        """ Client Handler """
        while True:
            recieved_data = hsock.recv(1024)
            decoded_data = recieved_data.decode("utf-8")
            str_i = str(index)
            if not decoded_data:
                print(f"[!] ERROR: Connection with client({self.ip_address}) {str_i} broken!")
                break
            if decoded_data.lower() == "exit":
                break
            if decoded_data.lower() == "kill server":
                sys.exit(0)
            print(f"[>] CLIENT {str_i}: -> {decoded_data}")

    def start_server(self, ssock):
        """ Starts Server """
        i = 1
        connection, sipaddr = ssock.accept()
        print(f"[!] INFO (CLIENT {i}): {self.ip_address} connection successful")
        self.handle_client(connection, sipaddr, i)

def main():
    """ Main Code """
    try:
        while True:
            server_object = StartServer()
            with socket.socket() as sock:
                sock.bind((HOST_SERVER, HOST_PORT))
                sock.listen(10)
                server_object.start_server(sock)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
            
