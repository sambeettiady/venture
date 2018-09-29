import pandas as pd
import numpy as np
import json

os.chdir('/home/sambeet/data/venture/')

companies = os.listdir('company/')
features = ['number_of_employees','founded_year','founded_month','founded_day','updated_at','milestones','products','category_code','competitions','offices','providerships','ipo','acquisitions','acquisition','investments','name','created_at','funding_rounds','total_money_raised']
rows = [0,20000,40000,60000,80000,len(companies)]

for j in range(6):
    for i,filename in zip(range(len(companies[rows[j]:rows[j+1]])),companies[rows[j]:rows[j+1]]):
        if (i%1000) == 0:
            print i
        with open('company/' + filename) as file:
            content = [x.replace('\\n','').replace('\\','').replace('S\'','').replace('\'','').strip('\n') for x in file.readlines()]
        try:
            content_json=json.loads(content[0])
        except:
            continue
        temp = pd.DataFrame.from_dict(content_json,orient='index')
        temp = temp.transpose()
        temp = temp[features]
        if i == 0:
            training = temp.copy()
        else:
            training = pd.concat([training,temp],axis=0,ignore_index=True)
    training.to_csv('venture_tabular_data_' + str(j) + '.csv',index=False)
