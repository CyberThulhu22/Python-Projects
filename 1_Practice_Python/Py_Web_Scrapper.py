#!/bin/python

# IMPORTS
import requests

# NOTES
"""
> Input list of websites.
> Run a test against websites to check if online
> Learn threading
> Load a wordlist for directory traversal
[null]Become a god

"""


website = input("Enter the website you want to do a get request \n #: ") 
r = requests.get(website)
