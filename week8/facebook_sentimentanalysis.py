# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:59:17 2020

@author: user
"""
#
#Steps
#1) add some data from facebook to excel sheet for processing
#2) import nltk library
#3) it is a library which is used to process human language
#4) sentiment analysis is working out on whether a sentence is positive, negative or neutral.
#5) we will use VADER (Valence Aware Dictionary and sentiment Reasoner)
#6) it also takes into account the intesity of sentiment
#7) VADER lexicon acts as dictonary 
#8) convert a excel sheet to data frame with the help of pandas
#9) a data frame is two dimensional structure in the form of a table.
     
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as a
nltk.downloader.download('vader_lexicon')
file='data_file.xslsx'
xl=pd.ExcelFile(file)       #reading file from excel
dfs=xl.prase(xl.sheet_names[0])     #parsing the excel sheet into data frames
dfs=list(dfs['Timeline'])
print(dfs)
sid=a()
str1='UTC+05:30'
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
