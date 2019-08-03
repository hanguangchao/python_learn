#!/usr/bin/env python3
# coding: utf-8

# In[6]:


import numpy as np

x = np.ones(3)            # Vector of three ones

y = np.array((2, 4, 6))   # Converts tuple (2, 4, 6) into array


# In[10]:


print(x)


# In[11]:


print(y)


# In[12]:


print(x + y)


# In[8]:


print(4 * x)


# In[9]:


print(np.sum(x * y))          # 向量内积 Inner product of x and y


# In[ ]:


print(np.sqrt(np.sum(x**2)))  # Norm of x, take one


# In[4]:


print(np.linalg.norm(x))      # Norm of x, take two
print(x / np.linalg.norm(x))


print(np.identity(4))

print(np.diag([1] * 4))