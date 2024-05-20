#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import pandas library

import pandas as pd
import os 

# LoadedCSV file into a pandas DataFrame

df = pd.read_csv('01.Data Cleaning and Preprocessing.csv')
df

# Display the first few rows of the DataFrame

df.head()


# In[5]:


# shows the descriptive datafame 

df.describe()


# In[7]:


# Here drop shows that to delete the duplicate of the rows in the dataframe

df=df.drop_duplicates()
df


# In[8]:


# shows the answers in boolean form which is either true or flase

df.isnull()


# In[9]:


# Shows how many null value are present in dataframe

df.isnull().sum()


# In[10]:


# Shows the opposite of nullfunction in boolean form which is either true or flse

df.notnull()


# In[11]:


# Shows the sum of all null value present in dataframe

df.isnull().sum().sum()


# In[12]:


# Filling the null value (1st method)

df2 = df.fillna(value=0)
df2


# In[15]:


# Shows all of the sum value present in dataframe

df.isnull().sum().sum()


# In[16]:


# Shows all of the sum value present in dataframe2

df2.isnull().sum().sum()


# In[18]:


# Filling the null value (2nd method by forward filling)

df3 = df.fillna(method='pad')
df3


# In[21]:


# Filling the null value (2nd method by backward filling)

df4 = df.fillna(method='bfill')
df4


# In[31]:


#import numpy 
#import matplotlib
#import scipy

import numpy as np
import matplotlib.pyplot as pit
from scipy import stats


# In[32]:


# Detect the Outliers using IQR

df2.columns


# In[34]:


# Here drop means remove | axis=1, represent column | inplace = true, means commiting change per minute

df2.drop(['Observation'], axis=1, inplace=True)
df2.columns


# In[35]:


# IQR applicable on numeric dataframe

Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3-Q1
print(IQR)


# In[36]:


# Formula 

df2 = df2[~((df2<(Q1-1.5*IQR))|(df2>(Q3+1.5*IQR))).any(axis=1)]
df2


# In[38]:


# Summary

df2.describe()


# In[ ]:




