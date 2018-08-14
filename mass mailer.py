from __future__ import print_function
import smtplib
import re
import io
import getpass
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import json


def emailAdd():
    scope = ["address of the web sheet"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('keyfile.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("sheet name").sheet1
    list_of_hashes =  sheet.get_all_records()
    email = list()
    number =len(list_of_hashes)

    for x in range(number):
        addressToVerify = list_of_hashes[x]['Email']
        email.append(addressToVerify)
    print (email)
    return email
def send_message(subject,msg,x):

    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.ehlo()
        email=raw_input("Enter your email")
        pswd = getpass.getpass('Enter your Password:')
        s.login(email,pswd)
        s.set_debuglevel(1)
        message = "Subject:{}\n\n{}".format(subject,msg)
        s.sendmail(email,x,message)
        s.quit()
    except:
        print("wrong")

x=emailAdd()
send_message("good night","This is a sample message from Club CodeFoster",x)
