import pandas as pd
import numpy as np
import os

os.chdir('/Users/sambeet/Desktop/venture/')

companies = os.listdir('articles/')

df = pd.DataFrame(columns=['company','article','text'])
for company in companies:
    if company != '.DS_Store':
        articles = os.listdir('articles/' + company + '/')
        text = []
        for article in articles:
            with open('articles/' + company + '/' + article,'r') as file:
                y = ''
                for x in file.readlines():
                    y = y + ' ' + x.replace('\\t','').replace('\\n','').strip()
                text.append(y)
        temp = pd.DataFrame({'company':[company]*len(articles),'article':articles,'text':text})
        df = pd.concat([df,temp],axis=0)
df.to_csv('articles.csv',index=False)
