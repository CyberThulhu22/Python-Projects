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
import sys
import os


class Drink:

    def __init__(self, full):
        self.full = full

    def refill(self):
        self.full = 100

    def drink(self):
        self.full -= 10

    def empty(self):
        self.full = False
        return self.full


class Mug:

    def __init__(self):
        pass

    def empty(self):
        print('''



 _                _
|:|              |:|____
|:|              |:|___.\
|:|              |:|   \.\
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def ten(self):
        print('''



 _                _
|:|              |:|____
|:|              |:|___.\
|:|              |:|   \.\
|:|              |:|   |:|
|:|       :      |:|   |:|
|:|   :   :   :  |:|   |:|
|:|   ::  ::  :: |:|   |:|
|:|   ::  ::  :: |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:| __:___:___:__|:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def twenty(self):
        print('''



 _                _
|:|              |:|____
|:|              |:|___.\
|:|              |:|   \.\
|:|              |:|   |:|
|:|  .   :   .   |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:| ::  ::  ::   |:|   |:|
|:|__:___:___:___|:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def thirty(self):
        print('''



 _                _
|:|              |:|____
|:|              |:|___.\
|:|              |:|   \.\
|:|  .   :   .   |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:| ::  ::  ::   |:|   |:|
|:|__:___:___:___|:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def forty(self):
        print('''



 _                _
|:|              |:|____
|:|              |:|___.\
|:|  .   :   .   |:|   \.\
|:|  ::  ::  ::  |:|   |:|
|:|  ::  ::  ::  |:|   |:|
|:| ::  ::  ::   |:|   |:|
|:|__:___:___:___|:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def fifty(self):
        print('''



 _                _
|:|              |:|____
|:|  .   :   .   |:|___.\
|:|  ::  ::  ::  |:|   \.\
|:|  ::  ::  ::  |:|   |:|
|:| ::  ::  ::   |:|   |:|
|:|__:___:___:___|:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def sixty(self):
        print('''



 _                _
|:|  .   :   .   |:|____
|:|  ::  ::  ::  |:|___.\
|:|  ::  ::  ::  |:|   \.\
|:| ::  ::  ::   |:|   |:|
|:|__:___:___:___|:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def seventy(self):
        print('''



 _   .   :   .    _
|:|  ::  ::  ::  |:|____
|:|  ::  ::  ::  |:|___.\
|:| ::  ::  ::   |:|   \.\
|:|__:___:___:___|:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def eighty(self):
        print('''


     .   :   .
 _   ::  ::  ::   _
|:|  ::  ::  ::  |:|____
|:| ::  ::  ::   |:|___.\
|:|__:___:___:___|:|   \.\
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def ninety(self):
        print('''

     .   :   .
     ::  ::  ::
 _   ::  ::  ::   _
|:| ::  ::  ::   |:|____
|:|__:___:___:___|:|___.\
|:|              |:|   \.\
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def hundo(self):
        print('''
     .   :   .
     ::  ::  ::
     ::  ::  ::
 _  ::  ::  ::    _
|:|__:___:___:___|:|____
|:|              |:|___.\
|:|              |:|   \.\
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|   |:|
|:|              |:|__/;/
|:.\____________/.:|__;/
 \________________/

''')

    def clear(self):
        os.system('cls')


try:
    Coffee = Drink(100)
    mug = Mug()
    Empty = 0
    mugnum = 1

    mug.clear()
    print("Time to drink some coffee!")
    mug.hundo()
    time.sleep(1)
    print("Pouring Coffee")
    time.sleep(1)
    print('Coffee is now', Coffee.full, '% full')
    mug.hundo()
    time.sleep(1)
    mug.clear()
    while Coffee.full >= 0:
        muglistdec = [mug.hundo, mug.ninety, mug.eighty, mug.seventy, mug.sixty,
                      mug.fifty, mug.forty, mug.thirty, mug.twenty, mug.ten,
                      mug.empty]
        if Coffee.full != Empty:
            mug.clear()
            Coffee.drink()
            print('Sipping Coffee...', Coffee.full, '% Full')
            muglistdec[mugnum]()
            time.sleep(0.5)
            mugnum += 1
            continue
        else:
            mug.clear()
            Coffee.refill()
            print('Refilling Coffee...')
            time.sleep(3)
            print('Coffee is full!', Coffee.full, '%')
            mug.hundo()
            time.sleep(1)
            mugnum = 1
            continue

except KeyboardInterrupt:
    print('You stopped drinking the coffee...')
    sys.exit()
    raise
