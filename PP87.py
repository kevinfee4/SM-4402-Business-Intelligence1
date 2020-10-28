#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df= pd.read_csv(Location)
df


# In[21]:


plt.scatter(df['hours'], df['grade'])


# In[ ]:




