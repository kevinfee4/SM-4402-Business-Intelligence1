#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3)
                               & (df['hours']>17),'busy', 'not busy')
df.tail(10)


# In[ ]:




