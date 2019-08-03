import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from math import sqrt


df = pd.read_excel(r'预测样本集.xlsx', sheetname='Sheet1')

x1 = df['avg_price_0.5']
x3 = df['avg_price_2']
x4 = df['avg_price_3']

s1 = df['0.5_price']
s3 = df['2_price']
s4 = df['3_price']

p = df['df']
pp = df['2_df']

fw1 =[]
for j in range(len(df)):
    pz = p[j]
    pzz = pp[j]

    g1 = x1[j]
    g3 = x3[j]
    g4 = x4[j]

    k1 = s1[j]
    k3 = s3[j]
    k4 = s4[j]

    X = df[['avg_price_0.5','0.5_price','avg_price_2','2_price','avg_price_3','3_price','df','2_df']]
    Y = df[['price_2']]

    regr = linear_model.LinearRegression()

    regr.fit(X,Y)

    a, b = regr.coef_, regr.intercept_
    a =a[0]
    print('***********a¡¢b***********')
    print("a" + str(a) + "  ||  b" + str(b))
    print('***********Ô¤²â***********')
    c = a[0] * g1 + a[1] * k1 + a[2] * g3 + a[3] * k3 + a[4] * g4 + a[5] * k4 + a[6] * pz + a[7] * pzz + b

    print(c)
    fw1.append(c)
    r = regr.score(X,Y,sample_weight=None)
    print(r)
yuce = pd.DataFrame(fw1)
yuce.to_excel('C:/Users/haozu/Desktop/5yuce.xlsx')

