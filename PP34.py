#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


bins = [0, 80, 100]
# Create names for the four groups
group_names = ['Fail', 'Pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins,labels=group_names)
df


# In[ ]:




