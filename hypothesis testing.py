#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from scipy import stats
sales = pd.read_excel("C:/Users/senth/OneDrive/sales.xlsx")
stats.ttest_ind(sales.before,sales.after)


# In[ ]:




