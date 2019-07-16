#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


content = pd.read_csv('mtcars - Data.csv')


# In[4]:


content.head()


# In[5]:


content.info()


# In[7]:


def mpg_level (row) :
    if row['mpg'] < 20 :
        return 'low'
    if row['mpg'] > 30 :
        return 'hard'
    return 'medium'


# In[9]:


df = pd.DataFrame(content)


# In[10]:


df.apply(lambda row : mpg_level(row), axis=1)


# In[11]:


df['mpg_level'] = df.apply(lambda row : mpg_level(row), axis=1)


# In[12]:


content.head()


# In[13]:


df


# In[15]:


df = pd.DataFrame(content, columns=['mpg', 'wt'])


# In[16]:


plt.scatter(df['wt'], df['mpg'])
plt.title('Rasio Mile per Galon berdasarkan Massa')
plt.xlabel('Massa')
plt.ylabel('Mile per Galon')


# In[17]:


# semakin besar massanya semakin boros menggunakan bahan bakar


# In[18]:


content['cyl'].value_counts()


# In[19]:


size = [14, 11, 7]
labels = ['Cylinder 8', 'Cylinder 4' , 'Cylinder 6']
explode = (0.1, 0, 0)
plt.pie(size, labels = labels, explode = explode, autopct = "%1.1f%%", shadow = True , startangle = 90 )
plt.show()


# In[20]:


def transmission (row) :
    if row[0] :
        return 'auto'
    return 'manual'


# In[21]:


df = pd.DataFrame(content, columns=['am', 'gear'])


# In[22]:


df['am'] = df.apply(lambda row : transmission(row), axis=1)


# In[23]:


df.head(8)


# In[24]:


pd.crosstab(df.am, df.gear, rownames=['transmission'], margins=True)


# In[ ]:




