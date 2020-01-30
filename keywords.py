import collections
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from dataframe import df_raw, df_no_stopwords, df_even, df_odd


df_raw = df_raw("./txts/")
df_no_stopwords = df_no_stopwords("./txts/")
df_even = df_even("./txts/")
df_odd = df_odd("./txts/")

dict = {'df_raw': df_raw, 'df_no_stopwords': df_no_stopwords, "df_even" : df_even, "df_odd" : df_odd}
# for key, value in dict.items():
#     text = key.text.str.cat(sep=' ')
#     tokens = word_tokenize(text)
#     frequency_dist = nltk.FreqDist(tokens)
#     top50 = sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]
#     with open ('commonwords_'+key+".txt", 'w') as out:
#         for item in top50:
#             out.write(item+"\n")
text = df_even.text.str.cat(sep=' ')
tokens = word_tokenize(text)
frequency_dist = nltk.FreqDist(tokens)
top50 = sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]
with open ('commonwords_df_even.txt', 'w') as out:
    for item in top50:
        out.write(item+"\n")

text = df_odd.text.str.cat(sep=' ')
tokens = word_tokenize(text)
frequency_dist = nltk.FreqDist(tokens)
top50 = sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]
with open ('commonwords_df_odd.txt', 'w') as out:
    for item in top50:
        out.write(item+"\n")


