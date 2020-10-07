#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,
                  columns=['Name','Grade','BS','MS','PhD'])
df


# In[4]:


df['Grade'].count()


# In[5]:


df['Grade'].mean()


# In[6]:


df['Grade'].std()


# In[7]:


df['Grade'].min()


# In[8]:


df['Grade'].max()


# In[9]:


df['Grade'].quantile(.25)


# In[10]:


df['Grade'].quantile(.5)


# In[11]:


df['Grade'].quantile(.75)


# In[12]:


df['Grade'].median()


# In[13]:


df['Grade'].mode()


# In[ ]:




