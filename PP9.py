#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/PVY01.xls"
df = pd.read_excel(Location)


# In[2]:


df.head()


# In[3]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[ ]:




