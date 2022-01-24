#!/usr/bin/env python
# coding: utf-8

# Referring to path of the folder we use for the data. I also use it to know if the file is connected correctly

# In[3]:


path = 'bitly_data.txt'


# In[4]:


open(path).readline()


# Use json module and its load function to convert JSON string into a python dictonary object 'records'

# In[5]:


import json


# In[6]:


records = [json.loads(line) for line in open(path)]


# Importing DataFrame and Series from Panda module, then importing entire pandas modules as pd

# In[10]:


from pandas import DataFrame, Series


# In[11]:


import pandas as pd


# Setting 'frame' to dataframe from the original set of records

# In[12]:


frame = DataFrame(records)


# In[13]:


frame


# Identify values we are looking for using method values_count

# In[14]:


frame['tz'][:10]


# In[15]:


tz_counts = frame['tz'].value_counts()


# In[16]:


tz_counts[:10]


# Using the fillna function to replace missing values and empty strings by boolean array indexing

# In[17]:


clean_tz = frame['tz'].fillna('Missing')


# In[18]:


clean_tz[clean_tz == ''] = 'Unknown'


# In[19]:


tz_counts = clean_tz.value_counts()


# In[20]:


tz_counts[:10]


# Making Figure 2-1 to indicate Top Time zones in the sample data

# In[21]:


tz_counts[:10].plot(kind='barh', rot = 0)


# Split pff the first token in the string data to make another summary of the user behavior

# In[22]:


results = Series([x.split()[0] for x in frame.a.dropna()])


# In[23]:


results[:5]


# In[24]:


results.value_counts()[:8]


# Assuming a user is on Windows if the string 'Windows' is the agent string, excluse some of the agents that are missing

# In[25]:


cframe = frame[frame.a.notnull()]


# Compute a value whether each row is Windows or not

# In[27]:


import numpy as np


# In[28]:


operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')


# In[29]:


operating_system[:5]


# Grouping data by its time zone column and the new list of operating systems

# In[30]:


by_tz_os = cframe.groupby(['tz', operating_system])


# In[31]:


agg_counts = by_tz_os.size().unstack().fillna(0)


# Select the top overall time zones

# In[32]:


indexer = agg_counts.sum(1).argsort()


# In[33]:


indexer[:10]


# In[34]:


count_subset = agg_counts.take(indexer)[-10:]


# In[35]:


count_subset


# Starting the formation of a bar chart

# In[36]:


count_subset.plot(kind='barh', stacked = True)


# Replicating Figure 2.3 in its entirety

# In[37]:


normed_subset = count_subset.div(count_subset.sum(1), axis = 0)


# In[38]:


normed_subset.plot(kind='barh', stacked = True)


# In[ ]:




