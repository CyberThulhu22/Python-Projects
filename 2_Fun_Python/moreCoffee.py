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

import json
import time
import sys
import os

def draw_left_side_mug():
    drawing_left = "   \n" * 4
    drawing_left += " _ \n"
    drawing_left += "|:|\n" * 10
    drawing_left += "|:.\____________/.:|__;/\n"
    drawing_left += " \________________/\n"
    return drawing_left.split("\n")

def draw_right_side_mug():
    drawing_right = "   \n" * 4
    drawing_right += " _\n"
    drawing_right += "|:|____ \n"
    drawing_right += "|:|___.\ \n"
    drawing_right += "|:|   \.\ \n"
    drawing_right += "|:|   |:| \n" * 6
    drawing_right += "|:|__/;/  \n\n"
    return drawing_right.split("\n")

def flattenNestedList(nestedList):
    flatList = []
    for elem in nestedList:
        if isinstance(elem, list):
            flatList.extend(flattenNestedList(elem))
        else:
            flatList.append(elem)    
    return flatList

def draw_content_inside_of_mug(num):
    if num == 11:
        return ("              \n" * 16).split("\n")
    drawing_content = "  .   :   .   \n  ::  ::  ::  \n  ::  ::  ::  \n ::  ::  ::   \n__:___:___:___".split("\n")
    empty_volume = ("              \n" * 11).split("\n")
    empty_volume.insert(num, drawing_content)
    flat_list = flattenNestedList(empty_volume)
    return flat_list

def main(num_list, speed):
    for i in num_list:
        os.system("cls")
        for count, value in enumerate(zip(draw_left_side_mug(), draw_content_inside_of_mug(i), draw_right_side_mug())):
            conv_value = json.dumps(value)
            print("".join(json.loads(conv_value)))
        time.sleep(speed)

if __name__ == "__main__":
    try:
        while True:
            main(reversed(range(0,12)), 0.2)
            time.sleep(2)
            main(range(0,12), 1)
            time.sleep(2)
    except KeyboardInterrupt:
        sys.exit(0)