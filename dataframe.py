import pandas as pd 
import os, os.path
import re
import collections
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#method to preprcoess data, remove erreneous characyers and standardize data, removes numbers

#each row is a text file
def df_raw(directory):
    num_files = len([name for name in os.listdir(directory)])

    df = pd.DataFrame()
    for i in range(1,num_files):
        name = str(i)+".txt"
        path = directory+name
        with open(path, 'r') as file: 
            text = ""
            for line in file:
                for word in line.lower().split(): 
                    #removes numbers and non alphabetic characters
                    regex = re.compile('[^a-zA-Z]')
                    word = regex.sub(' ', word)
                    text += word + " "  
        df = df.append([text],ignore_index=True)
    df.columns = ['text']
    df.to_csv('text_data.csv',index=False, encoding='utf-8')
    return df

#each row is a text file, without stop words
def df_no_stopwords(directory):
    stop_words = set(line.strip() for line in open('stopwords.txt'))
    stop_words = stop_words.union(set(stopwords.words('english')))
    num_files = len([name for name in os.listdir(directory)])
    # num_files = 2
    df = pd.DataFrame()
    for i in range(1,num_files):
        name = str(i)+".txt"
        path = directory+name
        text_alpha = []
        text = ""
        with open(path, 'r') as file: 
            for line in file:
                for word in line.lower().split(): 
                    #removes numbers and non alphabetic characters
                    regex = re.compile('[^a-zA-Z]')
                    word = regex.sub('', word)
                    if word != '' and word not in stop_words:
                        text += word + " "
            text_alpha.append(text)
        df = df.append(text_alpha,ignore_index=True)               
    df.columns = ['text']
    df.to_csv('text_no_stopwords.csv',index=False, encoding='utf-8')
    # print(df)
    return df

def df_even(directory):
    temp_df = df_no_stopwords(directory)
    list = []
    df = pd.DataFrame()
    for index, row in temp_df.iterrows():
        # print( len(row['text'].split(" ")))
        l = row['text'].split(" ")
        for i in range (0, len(l)-1):
            list.append(l[i]+l[i+1])
        df = df.append(list,ignore_index=True)               
    df.columns = ['text']
    df.to_csv('text_evenpairs.csv',index=False, encoding='utf-8')
    return df

def df_odd(directory):
    temp_df = df_no_stopwords(directory)
    list = []
    df = pd.DataFrame()

    for index, row in temp_df.iterrows():
        # print( len(row['text'].split(" ")))
        l = row['text'].split(" ")
        for i in range (1, len(l)-1):
            list.append(l[i]+l[i+1])
        df = df.append(list,ignore_index=True)               
    df.columns = ['text']
    df.to_csv('oddpairs.csv',index=False, encoding='utf-8')
    return df
