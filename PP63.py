#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "C:/Users/Kevin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0
df['gender_val'] = df['gender'].apply(score_to_numeric)
df.tail()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ exercise + hours + gender_val',
    data=df).fit()
result.summary()


# In[5]:


# the R-squared value increased from 0.664 to 0.665 when the gender value was included to the formula


# In[ ]:




