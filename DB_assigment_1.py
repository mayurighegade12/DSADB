#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import all required python libraries

#import numpy as np
import pandas as pd

import matplotlib 
from matplotlib import pyplot as plt 
# matplotlib.style.use('ggplot') 

import seaborn as sns


# In[ ]:





# In[8]:


# Loading data into dataframe
import io
df = pd.read_csv('C:/Users/coeco/OneDrive/Pictures/Desktop/Iris.csv') # csv file in dataframe called df 
# Dataset is now stored in a pandas Dataframe 

#classes = df['Species'].unique().tolist()
#classes


# In[9]:


#Information of the data present in dataset 
df.info()


# In[10]:


# Getting the dimension/shape of the data.
# Expect it to be 150 rows and 5 columns.
print(df.shape)


# In[11]:


# Print the first 20 data points -- the head of the dataset 
print(df.head(10))


# In[12]:


#Describing the data present in dataset
#use the describe function to describe some of the
# statistical properties of the data.
print(df.describe())


# In[13]:


# check the data types in the dataframe
df.dtypes


# In[14]:


df["Species"].unique()


# In[15]:


# use the groupby method to determine the class distribution 
print(df.groupby('Species').size())


# In[16]:


# Data points count value for each class labels.
df.Species.value_counts()


# In[17]:


# Checking for missing values
df.isnull().sum()


# In[18]:


#Turing categorical variables into quantitative variables

from sklearn import preprocessing 
#Label_encoder object knows how to understand word labels
label_encoder= preprocessing.LabelEncoder()

#Encode Labels in column 'Species' 
df['Species']=label_encoder.fit_transform(df['Species'])

df['Species'].unique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




