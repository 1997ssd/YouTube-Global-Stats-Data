#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as nd

df = pd.read_csv("C:\\Users\\shaqu\\Downloads\\Global YouTube Statistics.csv")

df.head(5)


# How many rows and columns are in Global Youtube Statistics

# In[23]:


df.shape


# Clean the data in order to remove all Not a Number Values
# This will allow for boolean indexing

# In[26]:


#Where Country has 'United Kingdom' fill True, else fill False, and only return favlues where Country is United Kingdom

#this fills NaN values in 'Country' with empty string
df['Country'] = df['Country'].fillna('')

#this creates new column 'UK Data' with True where 'Country' contains 'United Kingdom' else False
df['UK Data'] = df['Country'].apply(lambda x: 'United Kingdom' in x)

#creates new Dataframe from the UK data containing only rows where country is UK
uk_only = df[df['UK Data']]
print(uk_only)


# What was the average viewer number for UK youtubers (mean, median)

# In[30]:


mean_UK_video_views = uk_only['video views'].mean()
print(mean_UK_video_views)

median_UK_video_views = uk_only['video views'].median()
print(median_UK_video_views)

#round to nearest 00 and print as integer
rounded_mean = int(round(mean_UK_video_views, -2))
rounded_median = int(round(median_UK_video_views, -2))

print('The rounded mean is:' , rounded_mean)
print('The rounded median is:', rounded_median)


# Who are the top three most popular youtubers in the United Kingdom 

# In[29]:


#print just the top three youtubers from 'Youtuber' column
top_three_uk_youtubers = uk_only['Youtuber'].head(3)
print(top_three_uk_youtubers)


# In[ ]:




