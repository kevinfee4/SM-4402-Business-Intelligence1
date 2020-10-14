#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df = df.sort_values(by=['lname', 'age', 'grade'],
                    ascending=[True, True, True,])
df.head()


# In[ ]:




