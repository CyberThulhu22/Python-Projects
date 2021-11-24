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

import smtplib
import os
import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def emailText():
    smtp_ssl_host = 'mail.gmx.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = input('Enter your USERNAME or EMAIL:\n> ')
    password = getpass.getpass('Enter your PASSWORD:\n> ')
    sender = username
    targets = input('Who are you sending this email too?:\n> ')

    msg = MIMEText(input("What is your message?:\n> "))
    msg['Subject'] = input("Enter a SUBJECT:\n> ")
    msg['From'] = sender
    msg['To'] = targets

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()




def emailAttach():
    smtp_ssl_host = 'mail.gmx.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = input('Enter your USERNAME or EMAIL:\n> ')
    password = getpass.getpass('Enter your PASSWORD:\n> ')
    sender = username
    targets = input('Who are you sending this email too?:\n> ')

    msg = MIMEMultipart()
    msg['Subject'] = input('Enter a SUBJECT:\n> ')
    msg['From'] = sender
    msg['To'] = targets

    txt = MIMEText(input('Enter a Message:\n> '))
    msg.attach(txt)

    filepath = input('Enter File Path to the Attachment you want to add:\n> ')
    with open(filepath, 'rb') as f:
        img = MIMEImage(f.read())

    img.add_header('Content-Disposition',
                   'attachment',
                   filename=os.path.basename(filepath))

    msg.attach(img)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()


print("""
        Email Menu
===========================
1. Email Text
2. Email with Attachment\n> """)
choice = input()

if choice == '1':
    print("Emailing with just text")
    emailText()
elif choice == '2':
    print("Emailing with Attachment")
    emailAttach()
