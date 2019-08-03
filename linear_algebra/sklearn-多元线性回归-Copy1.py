#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  


# In[21]:


# 读入数据 
data = genfromtxt(r"/Users/han/Desktop/query_result.csv",delimiter=',')
print(data)


# In[22]:


# 切分数据
x_data = data[:,1:-1]
y_data = data[:,-1]
print(x_data)
print(y_data)


# In[23]:


# 创建模型
model = linear_model.LinearRegression()
model.fit(x_data, y_data)


# In[24]:


# 系数
print("coefficients:",model.coef_)

# 截距
print("intercept:",model.intercept_)

# 测试
# 8.83	77.9689	7.95	8.73	76.2129	54.51	2971.3401	6.67
#x_test = [[8.83,77.9689,7.95,8.73,76.2129,54.51,2971.3401,]]

x_test = [[5.89,34.70,5.66,5.05,25.47,41.50,1722.25,]]
predict = model.predict(x_test)
print("predict:",predict)


# In[25]:


# 1082	5.57	31.02	4.52	4.11	16.85	41.50	1722.25	6.09
#x_test = [[5.89,34.70,5.66,5.05,25.47,41.50,1722.25,]]
#x_test = [[5.57,31.02,4.52,4.11,16.85,41.50,1722.25,]]
x_test = x_data
predict = model.predict(x_test)

print("predict:",predict)


# In[19]:


plt.scatter(predict, y_data)
plt.show()


# In[ ]:





# In[ ]:





# In[7]:





print(model.score(x_data, y_data))


# In[ ]:




