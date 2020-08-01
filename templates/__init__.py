import csv
import time
import StreamingAPI
import SearchAPI
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import time
from textblob import TextBlob 
import pandas as pd
import string
from collections import defaultdict
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities
from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import roc_curve, auc
from sklearn import metrics
from scipy import interp
import sys
import json
from copy import deepcopy
from nltk.stem.porter import *
import nltk
import seaborn as sns
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities
from sklearn import linear_model
from sklearn.metrics import roc_curve, auc
import re
import operator 
from nltk.corpus import stopwords
import word_cloud
import test_plot
import word_barplot
import text_classifier
    

T = TweetTokenizer()
print("=========================================================================")
print("=========================================================================")
print("==============  TWITTER ANALYSIS FOR DISASTER MANAGEMENT  ===============")
print("=========================================================================")
print("=========================================================================")

x=input("Enter the lattitude value:")
y=input("Enter the longitude value:")
r=input("Enter the range (Eg: 20) :")
#BOSTON_GEOCODE = "42.362393,-71.062971,10km"
#CHICAGO_GEOCODE = "41.881832,-87.623177,10km"
#ROCKPORT_TEXAS_GEOCODE = "28.048611,-97.041111,10km"
#HOUSTON_TEXAS_GEOCODE = "29.789054,-95.387083,10km"
#MEXICO_CITY_GEOCODE = "19.432608,-99.133209,10km"
#Mumbai_GEOCODE = "19.075984,72.877656,10km"
#Bangalore_GEOCODE=str(x)+","+str(y)+","+str(r)+"km"
#newyork_geocode="40.712775,-74.005973,20km"
geocode=str(x)+","+str(y)+","+str(r)+"km"

keyword=[]
num=int(input("Enter number of keywords:"))
for i in range(0, num): # set up loop to run 5 times
	k = input('Please enter a keyword: ')
	keyword.append(k) # append to our_list

count=int(input("Enter the number of tweets u want to search:"))

if __name__ == '__main__':
    #keywords = ['']
    with open("disaster_tweets.csv", 'w') as csvfile:
        fieldnames = ['timestamp', 'location', 'text', 'coordinates', 'retweet']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for kw in keyword:
            tweets = SearchAPI.fetch(kw,geocode=geocode, count=count)
            yp=[]
            ys=[]
            for t in tweets:
                analysis = TextBlob(t.get('text').decode('utf-8'))
                yp.append(analysis.sentiment.polarity)
                ys.append(analysis.sentiment.subjectivity)
                writer.writerow(t)
            x=x=[i for i in range(len(yp))]
            #ys=np.cumsum(ys)
            yp=yp[::-1]
            y=[]
            value=0
            s=0
            for i in yp:
                if(i>0):
                    value=(0.5)
                elif(i<0):
                    value=(-0.6)
                else:
                    value=(-0.05)
                s+=value
                y.append(s)
            plt.plot(x, y, c="r", linestyle = '-', linewidth = 2)
            #plt.plot(ys)
            #plt.plot(x, ys, color='orange')
            plt.show
           
    word_cloud.wordcloud()
    word_barplot.barplot()    
    text_classifier.classifier()       
    test_plot.plotting()
    
    