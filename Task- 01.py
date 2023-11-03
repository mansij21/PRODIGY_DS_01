#!/usr/bin/env python
# coding: utf-8

# PRODIGY INFOTECH

# Author: Mansi Jadhav

# Data Science Intern

# Task - 01: Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_5871594.csv")


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.drop(['Unnamed: 5'], axis = 1)


# In[6]:


df.nunique()


# In[7]:


data = df['IncomeGroup'].value_counts()

# Define a list of colors for the bars
colors = ['lightgreen', 'lightcoral', 'lightpink', 'lightblue']

# Create a bar chart with specified colors
plt.figure(figsize=(10, 6))
data.plot(kind='bar', color=colors)
plt.title('Distribution of Countries by Income Group')
plt.xlabel('Income Group')
plt.ylabel('Number of Countries')
plt.xticks(rotation=45)
plt.show()


# In[8]:


data = df['IncomeGroup'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Countries by Income Group')
plt.show()


# In[9]:


data = df['Region'].value_counts()

# Define a list of colors for the bars
colors = ['#3366cc','#ccccff', '#ff8000', '#336600', 'lightcoral', 'lightpink', 'lightblue']

# Create a bar chart with specified colors
plt.figure(figsize=(10, 6))
data.plot(kind='bar', color=colors)
plt.title('Distribution of Region')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.show()


# In[10]:


import plotly.express as px
data = df['Country Code'].value_counts().reset_index()
data.columns = ['Country Code', 'Frequency']

# Create a treemap
fig = px.treemap(data, path=['Country Code'], values='Frequency')
fig.update_layout(margin=dict(t=0, b=0, r=0, l=0))
fig.show()

