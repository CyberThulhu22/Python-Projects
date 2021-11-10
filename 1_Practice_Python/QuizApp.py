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

# Imports
import sqlite3
import argparse
from sqlite3 import Error
from decimal import Decimal

# Standard Variables
__author__ = "Jesse Leverett"
__copyright__ = "Copyright (C) 2021 Jesse Leverett"
__license__ = "MIT License"
__version__ = "1.0"

def display_banner():
    print(f"""
******************************************************************
██╗    ██╗██╗██████╗ ███████╗██████╗ ██╗   ██╗██████╗ ██╗████████╗
██║    ██║██║██╔══██╗██╔════╝██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
██║ █╗ ██║██║██████╔╝█████╗  ██║  ██║██║   ██║██████╔╝██║   ██║
██║███╗██║██║██╔══██╗██╔══╝  ██║  ██║██║   ██║██╔═══╝ ██║   ██║
╚███╔███╔╝██║██║  ██║███████╗██████╔╝╚██████╔╝██║     ██║   ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝   ╚═╝
                 ██████╗ ██╗   ██╗██╗███████╗
                ██╔═══██╗██║   ██║██║╚══███╔╝
                ██║   ██║██║   ██║██║  ███╔╝
                ██║▄▄ ██║██║   ██║██║ ███╔╝
                ╚██████╔╝╚██████╔╝██║███████╗
                 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
******************************************************************
         Managment Server running version = {__version__}
******************************************************************
""")

# Instantiate Argument Parser
PROG_TEXT = ""
DESC_TEXT = ""
EPIL_TEXT = ""

parser = argparse.ArgumentParser(prog = PROG_TEXT,
                                description = DESC_TEXT,
                                epilog = EPIL_TEXT,
                                formatter_class = argparse.RawDescriptionHelpFormatter)

# Create Arguments
HELP_TEXT = ""

parser.add_argument('-o', metavar="", type=str, required=False, help=HELP_TEXT)
parser.add_argument('-db', metavar="sqlite.db", type=str, required=True, help=HELP_TEXT)

# Parse Arguments
args = parser.parse_args()

def wiredupitquiz():
    try:
        db_file = "C:\sqlite\database\quizdatabase.db"
        conn = sqlite3.connect(db_file)
        with conn:
            cur = conn.cursor()
            number = 1
            score = 0

            cur.execute('SELECT * FROM testquiz ORDER BY RANDOM()')
            data = cur.fetchall()

        for line in data: # For each line in the table from testquiz

            choice_a = line[2]
            choice_b = line[3]
            choice_c = line[4]
            choice_d = line[5]
            true_answer = line[6]

            print(f"{number}. {line[1]}", '-'*30)
            print(f"   A. {choice_a}")
            print(f"   B. {choice_b}")
            print(f"   C. {choice_c}")
            print(f"   D. {choice_d}")

    # Selecting an Answer Choice
            while True:
                choices = {'A': choice_a, 'B': choice_b, 'C': choice_c, 'D': choice_d}
                choice = input("Enter your answer here: ")
                if choice in choices:
                    if true_answer == choices[choice]:
                        print('CORRECT')
                        score = score + 1
                        break
                    else:
                        print('WRONG')
                        break
                else:
                    print("Not a valid answer choice!", choice)


            number = number + 1 #This is the next question number
            print("\n"*5)

        # Scoring what you made
        
        
        x = score
        y = len(data)
        precentage = Decimal(x/y)
        output = round(precentage,2) * 100
        print("You scored ", score, "out of", len(data))
        percentage = (score / len(data)) + (score % len(data) > 0.0) * 100
        print("You made a:", output, "%")

        #Testing a printout
        if output >= 90:
            print("Great Job!")
        elif 80 <= output < 90:
            print("Not bad!")
        elif 60 <= output < 80:
            print("You were cutting it close!")
        else:
            print("Try again. Better luck next time...")

    except Error as e:
        print(e)

def startquiz():
    print("MAIN MENU")
    print("-"*20)
    print("1. Begin Quiz")
    print("2. Exit")
    print("-"*20)
    menu_choices = {"1": 1, "2": 2}
    menu_choice = input("Enter what you want to do:")
    if menu_choices[menu_choice] == 1:
        wiredupitquiz()
    else:
        if menu_choices[menu_choice] == 2:
            exit()



if __name__ == "__main__":
    startquiz()
