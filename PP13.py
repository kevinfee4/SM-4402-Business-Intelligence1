#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
names = ['Nike','Adidas','New Balance','Puma','Reebok']
prices = [176,59,47,38,99]
PriceList = zip(names,prices)
df = pd.DataFrame(data = PriceList, columns=['Names','Prices'])


# In[5]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("datasets/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    all_data.describe()


# In[7]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("C:/Users/Kevin/Desktop/datasets/weekly_call_data/weekdata_000.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    all_data.describe()


# In[10]:


df.head()


# In[ ]:




