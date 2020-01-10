#!/usr/bin/env python
# coding: utf-8

# In[105]:


dataset = input()
with open(dataset, 'r') as f:
    data = []
    for i in f:
        s = i.rstrip()
        data.append(int(s))


# In[106]:


import numpy as np


# In[107]:


data


# In[113]:


print("{:.2f}".format(np.percentile(data, 90)))


# In[108]:


print("{:.2f}".format(np.median(data)))


# In[109]:


print("{:.2f}".format(np.max(data)))


# In[110]:


print("{:.2f}".format(np.min(data)))


# In[111]:


print("{:.2f}".format(np.mean(data)))


# In[ ]:




