import collections
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from dataframe import df

#use to download necessary packages , tokenizer and stopwords 
# nltk.download()

#function to split text into word

df = df("./txts/")


text = df.text.str.cat(sep=' ')
#function to split text into word
tokens = word_tokenize(text)
stop_words = set(line.strip() for line in open('stopwords.txt'))
stop_words = stop_words.union(set(stopwords.words('english')))
tokens = [w for w in tokens if not w in stop_words]
vocabulary = set(tokens)
# print(len(vocabulary))

frequency_dist = nltk.FreqDist(tokens)
top50 = sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]
# print(top50)
print(df)
with open ('commonwords.txt', 'w') as out:
    for item in top50:
        out.write(item+"\n")
