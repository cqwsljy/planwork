# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:36:55 2019

@author: Alpha
"""

import pandas as pd
import numpy as np
from numpy.linalg import solve
df = pd.read_excel("E:/Part-time/planwork/df.xlsx")
dfh = pd.read_excel("E:/Part-time/planwork/dfh.xlsx")
df = df.fillna(0)
df = df[df['skill'] == '甲']
datafreq = ['often','some','just']
a1 = sum(df['often'])
a2 = sum(df['some'])
a3 = sum(df['just'])
b = np.array([[5],[0],[0]])
A = np.array([[1,1,1],[a2,-2*a1,0],[0,a3,-3*a2]])
ws = solve(A,b)
ws[0][0] = np.ceil(ws[0][0])
ws[1][0] = np.ceil(ws[1][0])
ws[2][0] = np.ceil(ws[2][0])

##根据历史调整 w,pn 按照上班属性分组，当前值班比例
N = sum(df['date'])
if N == 0:
    pn = [ws[0][0],ws[1][0],ws[2][0]]  
else:
    pn = [sum(df[df['often'] == 1]['date'])/N,sum(df[df['some'] == 1]['date'])/N,sum(df[df['just'] == 1]['date'])/N]



w = [ws[0][0],max(min(5-ws[0][0],ws[1][0]),0),max(0,ws[0][0]+ws[1][0])]

for i in range(ws.shape[0]):
    print(i)
    dftemp = df[df[datafreq[i]] == 1]
    dftemp = dftemp.sort_values(by='date')
    if w[i] > 0:
        data = dfh['姓名'].tolist()
        index = dftemp.index[0:int(w[i])]
        data.extend(df['姓名'][index].tolist())
        dfh = pd.DataFrame(data,columns=['姓名'])
        df['date'][index] = df['date'][index] + 1
        
df.to_excel("E:/Part-time/planwork/df.xlsx")
dfh.to_excel("E:/Part-time/planwork/dfh.xlsx")