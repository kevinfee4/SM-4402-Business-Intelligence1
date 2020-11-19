#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df['Cars Sold'].mean()


# In[4]:


df['Cars Sold'].max()


# In[5]:


df['Cars Sold'].min()


# In[6]:


gender_carsSold = df['Cars Sold'].groupby(df['Gender'])
gender_carsSold.mean()


# In[7]:


df.loc[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


df['Years Experience'].mean()


# In[9]:


df.loc[df['Cars Sold']>3]['Years Experience'].mean()


# In[14]:


pd.pivot_table(df,
               values=['Cars Sold'],
               index=['SalesTraining'],
               aggfunc='mean')


# In[18]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/Kevin/Desktop/datasets/axisdata.csv"
df= pd.read_csv(Location)
plt.scatter(df['Hours Worked'], df['Cars Sold'])


# In[11]:


plt.scatter(df['Years Experience'], df['Cars Sold'])


# In[ ]:





# In[ ]:




