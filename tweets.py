#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
dataset = pd.read_csv('tweets.csv',encoding = 'ISO-8859-1')
dataset.head()


# In[5]:


import re
def clean_text(text):
    text = re.sub(r'RT',' ',text)
    #fix &
    text = re.sub(r'&amp;',',text')
    #remove punctuation
    text = re.sub(r'[?!.;:,#@-]','',text)
    #convert to lowercase to maintain consistency
    text = text.lower()
    return text


# In[7]:


get_ipython().system('pip install wordcloud')


# In[8]:


#import list of stopwords
from wordcloud import STOPWORDS
print(STOPWORDS)


# In[ ]:




