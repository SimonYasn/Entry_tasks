#!/usr/bin/env python
# coding: utf-8

# In[788]:


f  = open('txt.txt', 'r')


# In[789]:


for i in f:
    s = i.rstrip().split()
    data1.append(s)


# In[ ]:





# In[ ]:





# In[790]:


data_res= []


# In[791]:


for i in data1:
    data_1 = []
    time_start = i[0].split(':')
    time_start = int(time_start[0])*60 + int(time_start[1])
    time_end = i[1].split(':')
    time_end = int(time_end[0])*60 + int(time_end[1])
    data_1 = [i for i in range(time_start,time_end)]
    if time_start == time_end:
        data_1.append(time_start)
    for i in data_1:
        data_res.append(i)


# In[792]:


max_count = []
for i in data_res:
    max_count.append(data_res.count(i))
    


# In[793]:


max_count = sorted(max_count, reverse=True)


# In[794]:


max= max_count[0]
end_data = []


# In[795]:


for i in data_res:
    if data_res.count(i)==max:
        end_data.append(i)
    


# In[796]:


end_data = sorted(list(set(end_data)))


# In[797]:


end_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[706]:





# In[707]:





# In[708]:





# In[709]:





# In[ ]:





# In[710]:





# In[711]:





# In[712]:





# In[713]:





# In[714]:





# In[715]:





# In[643]:





# In[645]:





# In[ ]:





# In[723]:





# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[587]:





# In[588]:





# In[589]:





# In[590]:





# In[591]:





# In[ ]:





# In[ ]:





# In[ ]:




