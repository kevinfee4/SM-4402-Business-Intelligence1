#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[2]:


df.head()


# In[3]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[4]:


df.head()


# In[5]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/smallgrades.csv"
# To add headers as we load the data...
df = pd.read_csv(Location, names=['Names','Grades'])
# To add headers to a dataframe
df.columns = ['Names','Grades']


# In[6]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/.ipynb_checkpoints/ch2_02_saveCsv-checkpoint.ipynb"
df = pd.read_csv(Location, header=None)


# In[7]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/all_040_in_12.P1.csv"
df = pd.read_csv(Location, header=None)


# In[8]:


df.head()


# In[ ]:




