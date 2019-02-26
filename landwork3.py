# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:45:43 2019

@author: Alpha
"""

import pandas as pd
import numpy as np
import copy 
p = [0.7,0.3]
df = pd.read_excel("C:/Users/Alpha/Desktop/planwork/df.xlsx")
#df['proActual'] = 0
#df['proStandard'] = 0
dfh = pd.read_excel("C:/Users/Alpha/Desktop/planwork/dfh.xlsx")

df = df.fillna(0)
df = df[df['skill'] == '甲']
datafreq = ['often','some']
a1 = np.double(sum(df['often']))
a2 = np.double(sum(df['some']))
a = [a1,a2]
N = np.double(sum(df['date']))

if N == 0:
    for i in range(len(datafreq)):
        df.loc[df[datafreq[i]]==1,'proStandard'] =  p[i]/a[i]
    index = copy.deepcopy(df.index)
    index = np.random.permutation(index)
    data = dfh['姓名'].tolist()
    data.append(df['姓名'][index[0]])
    dfh = pd.DataFrame(data,columns=['姓名'])
    df.loc[index[0],'date'] = df['date'][index[0]] + 1
    N = sum(df['date'])
    df['proActual'] = df['date'] / N
    df['dateDiff'] = df['proActual'] - df['proStandard']
        
else:
    c = df['proActual'] < df['proStandard']
    dftemp = df[c]
    dftemp = dftemp.sort_values('dateDiff')
    index = copy.deepcopy(dftemp.index)
    index = np.random.permutation(index)
    data = dfh['姓名'].tolist()
    data.append(df['姓名'][index[0]])
    dfh = pd.DataFrame(data,columns=['姓名'])
    df.loc[index[0],'date'] = df['date'][index[0]] + 1
    N = sum(df['date'])
    df['proActual'] = df['date'] / N
    df['dateDiff'] = df['proActual'] - df['proStandard']
    print(df)
    
    
df.to_excel("C:/Users/Alpha/Desktop/planwork//df.xlsx",index=False)
dfh.to_excel("C:/Users/Alpha/Desktop/planwork/dfh.xlsx",index=False)