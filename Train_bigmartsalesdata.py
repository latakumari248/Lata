#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'in line')
import warnings # Ignores any warning
warnings.filterwarnings("ignore")


# In[ ]:


os.getcwd()


# In[7]:


df=pd.read_csv("C://Users//BRIEF//OneDrive//Desktop//Data Science//Python _IMS Class//Bigmart sales predication_analytics Vidhya//train_v9rqX0R.csv")


# In[8]:


df


# In[9]:


df.head(5)


# In[10]:


df.tail(5)


# In[11]:


df.info()            # datatype of attributes


# In[12]:



df.describe()                          # statistical info


# In[13]:


df.nunique()                                   # check unique values in data set


# # Preprocessing the data set

# In[14]:


df.isnull().sum()                              # check for null values


# In[15]:


cat_col= []                                                # check the categorical attributes
for x in df.dtypes.index:
    if df.dtypes[x]=='object':
        cat_col.append(x)
cat_col


# In[16]:


cat_col.remove('Item_Identifier')
cat_col.remove('Outlet_Identifier')
cat_col


# In[14]:


for col in cat_col:
    print(col)
    print(df[col].value_counts())
    print()


# In[17]:


# Fill the missing values

item_weight_mean = df.pivot_table(values="Item_Weight",index ="Item_Identifier")
item_weight_mean


# In[18]:


miss_bool = df['Item_Weight'].isnull()
miss_bool


# In[32]:


for i, item in enumerate(df['Item_Identifier']):
    if miss_bool[i]:
        if item in item_weight_mean:
            df['Item_Weight'][i] = item_weight_mean.loc[item]['Item_Weight']
        else:
             df['Item_Weight'][i] = 0


# In[33]:


df['Item_Weight'].isnull().sum()


# In[34]:


outlet_size_mode=df.pivot_table(values = 'Outlet_Size', columns='Outlet_Type',aggfunc=(lambda x: x.mode()[0]))
outlet_size_mode


# In[35]:


miss_bool = df['Outlet_Size'].isnull()
df.loc[miss_bool,'Outlet_Size']=df.loc[miss_bool,'Outlet_Type'].apply(lambda x: outlet_size_mode[x])


# In[36]:


df['Outlet_Size'].isnull().sum()


# In[37]:


sum(df['Item_Visibility']==0)


# In[38]:


df.loc[:'Item_Visibility '].replace([0],[df['Item_Visibility'].mean()],inplace=True)        # replace zeros with mean


# In[39]:


sum(df['Item_Visibility']==0)


# In[48]:


# combine item fat content
df['Item_Fat_Content']= df['Item_Fat_Content'].replace({'LF':'Low Fat','reg': 'Regular','low fat':'Low Fat'})

df['Item_Fat_Content'].value_counts()


# # Creation of New Attributes

# In[46]:


df['New_item_Type'] = df['Item_Identifier'].apply(lambda x: x[:2])

df['New_item_Type']


# In[44]:


df.loc[df['New_item_Type']=='Non-consumble','Item_Fat_Content']='Non- Edible'
df['Item_Fat_Content'].value_counts()


# In[60]:


df['New_item_Type']= df['New_item_Type'].map({'fd':'food','NC':'Non-consumble','DR':'Drinks'})


# In[61]:


df['New_item_Type'].value_counts()


# In[62]:


# Create small values for establishment year
df['Outlet_Years']= 2013-df['Outlet_Establishment_Year']


# In[63]:


df['Outlet_Years']


# In[5]:


df.head()


# # Exploratory Data analysis

# In[73]:


sns.distplot(df['Item_Weight'])


# In[74]:


sns.distplot(df['Item_Visibility'])


# In[75]:


sns.distplot(df['Item_Outlet_Sales'])


# In[76]:


sns.countplot(df['Item_Fat_Content'])


# In[69]:


sns.distplot(df['Item_MRP'])


# In[4]:


# plt.figure(figsize=(15,5)) 
l =  list(df['Item_Type'].unique())
chart = sns.countplot(df['Item_Type'])
chart.set_xticklabels(labels=1,rotation=90)


# In[ ]:





# In[ ]:




