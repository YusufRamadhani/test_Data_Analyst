#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


content = pd.read_csv('Inflasi - Inflasi.csv')


# In[3]:


content.head(15)


# In[4]:


content.info()


# In[5]:


content['Inflasi'] = content.Inflasi.str.replace('%','').astype(float) # trim '%' agar object bisa cast to float


# In[6]:


content.info()


# In[7]:


content.head(7)


# In[8]:


df = pd.DataFrame(content)
df.describe()


# In[9]:


import matplotlib.pyplot as plt


# In[10]:


inflasi = df['Inflasi']
plt.ylim(df['Inflasi'].min(),df['Inflasi'].max())
plt.xlim(df['Inflasi'].count(), 0) # dibalik agar data bisa dibaca dr 2003 -> 2019
plt.plot(df['Inflasi'], color='red') 
plt.xlabel('Jumlah Data')
plt.ylabel('Tingkat Inflasi')
plt.show()


# In[11]:


inflasi = df['Inflasi']
plt.ylim(df['Inflasi'].min(),df['Inflasi'].max())
plt.xlim(df['Inflasi'].count(), 0) # dibalik agar data bisa dibaca 2003 - 2019
sma_20 = df['Inflasi'].rolling(window=20).mean() #dataframe.rolling() => window calculation
ema_60 = df['Inflasi'].ewm(span=60).mean()  # dataframe.ewm() => exponential weighted 

plt.plot(inflasi, color='red') 
plt.plot(sma_20, label='20 SMA', color='blue') # Simple Moving Average
plt.plot(ema_60, label='60 EMA', color='green') # Exponential Moving Average
plt.xlabel('Jumlah Data')
plt.ylabel('Tingkat Inflasi')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




