from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
from nltk.stem.porter import PorterStemmer
import matplotlib.pyplot as plt

def wordcloud():
    train = pd.read_csv("E:\\Deep Learning\Azure\\disaster_tweets.csv")
    train.head()
    
    def remove_pattern(input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)        
        return input_txt 

    train['tidy_tweet'] = np.vectorize(remove_pattern)(train['text'], "@[\w]*")
    train['tidy_tweet'] = train['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")
    train['tidy_tweet'] = train['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    train.head()

    tokenized_tweet = train['tidy_tweet'].apply(lambda x: x.split())
    tokenized_tweet.head()
    stemmer = PorterStemmer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
    tokenized_tweet.head()
         
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
        train['tidy_tweet'] = tokenized_tweet
    
    all_words = ' '.join([text for text in train['tidy_tweet']])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()