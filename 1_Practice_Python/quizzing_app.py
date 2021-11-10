#!/usr/bin/env python3
#-*- Coding: utf-8 -*-

"""
NAME: quizzing_app.py
VERSION: 1.0
AUTHOR: Jesse Leverett (CyberThulhu)
STATUS: Building Initial code framework
DESCRIPTION: Application to Create a Quiz from a Database
TO-DO:
    [ ] Build Initial Code Framework
    [ ] Build Database with Questions and Answers
COPYRIGHT © 2021 Jesse Leverett
"""

# Standard Variables
__author__ = "Jesse Leverett"
__copyright__ = "Copyright (C) 2021 Jesse Leverett"
__license__ = "MIT License"
__version__ = "1.0"

# Imports
import sys
import json
import time
import logging
import sqlite3
import argparse
from decimal import Decimal
from colorama import init, Fore, Back, Style
import colorama

# Initialize Colorama
init()

def display_banner():
    print(Fore.GREEN + f"""
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
            Managment Server running version {__version__}
******************************************************************
""" + Fore.RESET)

# Instantiate Argument Parser
PROG_TEXT = "quizzing_app"
DESC_TEXT = "Quizzing Application"
EPIL_TEXT = f"{__copyright__}"

parser = argparse.ArgumentParser(prog = PROG_TEXT,
                                description = DESC_TEXT,
                                epilog = EPIL_TEXT,
                                formatter_class = argparse.RawDescriptionHelpFormatter)

# Create Arguments
HELP_TEXT = ""

parser.add_argument('-o', dest="output_file", metavar="", type=str, required=False, help=HELP_TEXT)
parser.add_argument('-db', dest="database_file", metavar="sqlite.db", type=str, required=False, help=HELP_TEXT)

# Parse Arguments
args = parser.parse_args()

class LoadQuestion:
    """ Loads a Question Object """
    def __init__(self, load_question:str) -> None:
        self.load_question = load_question

    def format_qlist(self) -> list:
        """ Formats data from table into list """
        pass

    def answer_question(self) -> str:
        """ Returns Answer of the Question """
        pass

    def score_question(self) -> int:
        """ Returns score for Question """
        pass

def load_database(db_file:str=args.database_file):
    """ Loads a Database Question Bank """
    connect_to_database = sqlite3.connect(db_file)
    database_cursor = connect_to_database.cursor()
    database_cursor.execute("SELECT * FROM (?) ORDER BY RANDOM()")
    database_data = database_cursor.fetchall()
    return database_data

def run() -> None:
    """ Running Components """


def main() -> None:
    """ Main Program """
    display_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)