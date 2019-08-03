#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/Qinbf/tf-model-zoo/master/README_IMG/01.jpg)
# AI MOOC： **www.ai-xlab.com**  
# 如果你也是AI爱好者，可以添加我的微信一起交流：**sdxxqbf**

# In[37]:


import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  


# In[38]:


# 读入数据 
data = genfromtxt(r"/Users/han/Code/GitPro/python_learn/linear_algebra/1.csv",delimiter=',')
print(data)


# In[39]:


# 切分数据
x_data = data[:,:-1]
y_data = data[:,-1]
print(x_data)
print(y_data)


# In[40]:


# 创建模型
model = linear_model.LinearRegression()
model.fit(x_data, y_data)


# In[43]:


# 系数
print("coefficients:",model.coef_)

# 截距
print("intercept:",model.intercept_)

# 测试
# 8.83	77.9689	7.95	8.73	76.2129	54.51	2971.3401	6.67
x_test = [[8.83,77.9689,7.95,8.73,76.2129,54.51,2971.3401,]]
predict = model.predict(x_test)
print("predict:",predict)


# In[42]:


ax = plt.figure().add_subplot(111, projection = '3d') 
ax.scatter(x_data[:,0], x_data[:,1], y_data, c = 'r', marker = 'o', s = 100) #点为红色三角形  
x0 = x_data[:,0]
x1 = x_data[:,1]
x2 = x_data[:,2]
x3 = x_data[:,3]
x4 = x_data[:,4]
x5 = x_data[:,5]
x6 = x_data[:,6]
# 生成网格矩阵
x0, x1 = np.meshgrid(x0, x1)
#z = model.intercept_ + x0*model.coef_[0] + x1*model.coef_[1]
z = model.intercept_ + x0*model.coef_[0] + x1*model.coef_[1] + x2*model.coef_[2] + x3*model.coef_[3] + x4*model.coef_[4] + x5*model.coef_[5] + x6*model.coef_[6]
# 画3D图
ax.plot_surface(x0, x1, z)
#设置坐标轴  
ax.set_xlabel('x')  
ax.set_ylabel('y')  
ax.set_zlabel('z')  
  
#显示图像  
plt.show()  



