#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install seaborn


# In[2]:


import seaborn as sns


# In[3]:


#binomial distribution


# In[4]:


from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0,size=100)
data_binom


# In[10]:


ax = sns.distplot(data_binom,kde=False,color='blue')
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')


# In[7]:


#normal distribution


# In[8]:


from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=1000,loc=0,scale=1)
data_normal


# In[11]:


ax = sns.distplot(data_normal,
 bins=100,
 kde=True)
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


# In[ ]:




