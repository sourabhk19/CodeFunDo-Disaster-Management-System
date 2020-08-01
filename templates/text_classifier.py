from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
import csv
def classifier(): 
        value=0
        with open('classifier_trainset.csv', 'r') as fp:
                cl = NaiveBayesClassifier(fp, format="csv")
        with open('classifier_testset.csv','r') as f:
                value=cl.accuracy(f)*100
        print "\nAccuracy=",value,"%"
        
        relevant=0
        nt_relevant=0
       
        r=['']
        cnt=1
        print("\n=====================RELEVANT TWEETS========================\n")
        df=pd.read_csv('disaster_tweets.csv')
        for file in df["text"]:
                if(cl.classify(file.decode('utf-8'))=='Relevant'):
                        relevant+=1
                        r.append('Relevant')                        
                        print cnt,".",file,"\n"
                        cnt+=1
                else:
                        nt_relevant+=1
                        r.append('Not Relevant')
                        
       
       
        csvfile = 'disaster_tweets.csv'
        with open(csvfile, 'rb') as fin, open('new_'+csvfile, 'wb') as fout:
                reader = csv.reader(fin,  lineterminator='\n')
                writer = csv.writer(fout, lineterminator='\n')
                new_heading='Relevance'
                writer.writerow(next(reader) + [new_heading])
                i=0
                for row, val in zip(reader, r):
                        writer.writerow(row + [r[i]])
                        i=i+1
                #df.to_csv('output.csv')
        print("Relevant:",relevant)
        print("Not Relevant:",nt_relevant)


    
   