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
class Person:
    def __init__(self, f_name, l_name, health, sanity):
        self.f_name = f_name
        self.l_name = l_name
        self.health = health
        self.sanity = sanity

class Equipment:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class Room:
    def __init__(self, name):
        self.name = name

