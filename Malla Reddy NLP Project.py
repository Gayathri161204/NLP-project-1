#!/usr/bin/env python
# coding: utf-8

# # Day 1

# ## Importing the data 
# 
# Link to data - https://www.kaggle.com/datasets/alfathterry/bbc-full-text-document-classification?resource=download

# In[3]:


import pandas as pd 
import numpy as np 


# In[4]:


df = pd.read_csv('bbc_data.csv')


# In[5]:


df


# In[6]:


df['labels'].value_counts()


# In[8]:


df['labels'].unique()


# In[9]:


df['data'].nunique()


# In[10]:


df.isna().sum()


# In[11]:


df['labels'].value_counts()


# In[ ]:




