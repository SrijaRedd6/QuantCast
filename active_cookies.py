#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Displaying most active cookies
Created on Sat Feb 12 11:18:37 2022
@author: srija
"""

import sys
import pandas as pd
from datetime import date,datetime,time

def check(): #function to check arguments from Command Line Interface
    print("Usage: {sys.argv[0]} <csv_file> -d \"yyyy-mm-dd\"")


# Check command line arguments.
if len(sys.argv) != 4 or sys.argv[2] != '-d':
    check()
    exit(1)
    
req_datetime=sys.argv[3]#read required date.
data=pd.read_csv(sys.argv[1],encoding='utf-8')#read csv file
df=pd.DataFrame(data)
df[["date","time"]]=df['timestamp'].str.split("T",expand=True) #Splitting timestamp column with date and time
df.drop(df[df['date'] != req_datetime].index, inplace = True)  #Dropping rows that are not equal to required date
df2=df["cookie"].mode()#Get the most used cookies
print(df2.to_string(index=False))
