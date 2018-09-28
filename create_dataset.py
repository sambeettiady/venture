import pandas as pd
import numpy as np
import json

os.chdir('/Users/sambeet/Desktop/venture/')

companies = os.listdir('company/')
features = ['number_of_employees','founded_year','founded_month','founded_day','updated_at','milestones','products','category_code','competitions','offices','providerships','ipo','acquisitions','acquisition','investments','name','created_at','funding_rounds','total_money_raised']
for filename in companies:
    with open('company/' + filename) as file:
        content = [x.replace('\\n','').replace('\\','').replace('S\'','').replace('\'','').strip('\n') for x in file.readlines()]
    try:
        content_json=json.loads(content[0])
    except:
        continue
    temp = pd.DataFrame.from_dict(content_json,orient='index')
    temp = temp.transpose()
    temp = temp[features]
    if filename == 'aginfolink':
        training = temp.copy()
    else:
        training = pd.concat([training,temp],axis=0,ignore_index=True)
training.to_csv('tabular_data.csv',index=False)
