import re
import pandas as pd
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
from collections import Counter
import operator 
import numpy as np

def barplot():    
    #word bar plot
    emoticons_str = r"""
    (?:
    [:=;] # Eyes
    [oO\-]? # Nose (optional)
    [D\)\]\(\]/\\OpP] # Mouth
    )"""
    
    regex_str = [
        emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
     
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]
    
    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)    
    
    def tokenize(s):
        return tokens_re.findall(s)    
    punctuation = list(string.punctuation)
    
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    
    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens
    
    df = pd.read_csv("E:\\Deep Learning\Azure\\disaster_tweets.csv",error_bad_lines=False)
    print (df.columns)
    count_all = Counter()
    df = df[["text"]]
    print ("Total tweets: %d" % len(df))
    df = df.drop_duplicates(subset = ["text"]).reset_index() #this also resets the index otherwise the numbers will have gaps
    print ("Total unique tweets: %d" % len(df))
    word_counter = {}
    
    for i in df["text"]:           
            terms_stop =[terms for terms in preprocess(i) if terms not in stop]
            #print(terms_stop)
            for word in terms_stop:
                    if (word in word_counter) and (len(word)>3):
                            word_counter[word]+=1
                    else:
                            word_counter[word]=1
    popular_words= sorted(word_counter.items(), key=operator.itemgetter(1),reverse=True)
    top= popular_words[:10]
    print(top)
    
    Words = list(zip(*top))[0]
    Count = list(zip(*top))[1]
    x_pos = np.arange(len(Words)) 
    
    # calculate slope and intercept for the linear trend line
    slope, intercept = np.polyfit(x_pos, Count, 1)
    trendline = intercept + (slope * x_pos)
    
    plt.plot(x_pos, trendline, color='red', linestyle='--')    
    plt.bar(x_pos, Count,align='center')
    plt.xticks(x_pos, Words,rotation=90) 
    plt.ylabel('Count')
    plt.show()