import pandas as pd 
import os, os.path


#method to preprcoess data, remove erreneous characyers and standardize data

def df(directory):
    num_files = len([name for name in os.listdir(directory)])

    df = pd.DataFrame()
    for i in range(1,num_files):
        name = str(i)+".txt"
        path = directory+name
        with open(path, 'r') as file: 
            text = ""
            for line in file:
                for word in line.split(): 
                    word = word.replace(".","")
                    word = word.replace(",","")
                    word = word.replace(":","")
                    word = word.replace("\"","")
                    word = word.replace("!","")
                    word = word.replace("â€œ","")
                    word = word.replace("â€˜","")
                    word = word.replace("*","")
                    text += word + " "  
        df = df.append([text],ignore_index=True)
    df.columns = ['text']
    df.to_csv('text_data.csv',index=False, encoding='utf-8')
    return df


# df = df('./txts/')