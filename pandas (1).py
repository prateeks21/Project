#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dict1={"Name":['Prateek','Rahul','Roshan','Abhishek'],
      "Marks":['98','45','76','64'],
      "City":['Varanasi','Delhi','Mumbai','Lucknow']}


# In[3]:


df=pd.DataFrame(dict1)


# In[4]:


df


# In[5]:


df.to_csv('Friends.csv')


# In[6]:


df.to_csv('Friendsnoindex.csv', index=False)


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.describe()


# In[10]:


df['Name']


# In[11]:


df['Name'][2]


# In[12]:


df['Name'][2]='Golesar'


# In[13]:


df


# In[14]:


df.to_csv('namechange.csv')


# In[15]:


df.index=['1st','2nd','3rd','4th']


# In[16]:


df


# In[17]:


df.to_csv('newownchanges', index=False)


# In[ ]:





# In[ ]:





# In[18]:


ser=pd.Series(np.random.rand(23))


# In[19]:


ser


# In[20]:


type(ser)


# In[21]:


newdf=pd.DataFrame(np.random.rand(40,4), index=np.arange(40))


# In[22]:


newdf


# In[23]:


newdf.head()


# In[24]:


type(newdf)


# In[25]:


newdf.describe()


# In[26]:


newdf.dtypes


# In[27]:


newdf[2][2]="Prateek"


# In[28]:


newdf.head()


# In[29]:


newdf.index


# In[30]:


newdf.columns


# In[31]:


newdf.to_numpy()


# In[32]:


newdf.head()


# In[33]:


newdf[2][2]='34'


# In[34]:


newdf.head()


# In[35]:


newdf.T.head()


# In[36]:


newdf.sort_index(axis=0, ascending=False) #axis=0 means row


# In[37]:


newdf.head()


# In[38]:


newdf[0]


# In[39]:


type(newdf[0])


# In[40]:


#dont do newdf2=newdf like statement otherwise if you change the newdf2 then it automatically change the newdf
#if you want to do this then do this
newdf2=newdf.copy()


# In[41]:


newdf2.head()


# In[42]:


newdf.columns=['a','b','c','d'] #you can also do newdf.columns(list("abcd"))


# In[43]:


newdf.head(1)


# In[44]:


newdf.loc[0,0]=1


# In[45]:


newdf.head()


# In[46]:


newdf.loc[0,'a']


# In[47]:


newdf=newdf.drop(0, axis=1).head()


# In[48]:


newdf.head()


# In[49]:


newdf.loc[[3,4],['b','c']]


# In[50]:


newdf.loc[[3,4],:]


# In[51]:


newdf.loc[newdf['a']<0.9]


# In[52]:


newdf.loc[(newdf['a']<0.9) & ( newdf['d']>0.2)]


# In[53]:


newdf.loc[0,'c']


# In[54]:


newdf.iloc[1,1]


# In[55]:


newdf.drop(['a','c'], axis=1) #but if you use statement newdf.drop(['a','c'], axis=1 , inplace=True) then it also chages 
# the original dataframe


# In[56]:


newdf.head()


# In[57]:


newdf.reset_index(drop=True, inplace=True)


# In[58]:


newdf


# In[59]:


newdff=pd.DataFrame(np.random.rand(40,4), index=np.arange(40))


# In[60]:


newdff.head()


# In[61]:


newdff.head()


# In[62]:


newdf.head()


# In[63]:


newdf.columns=[0,1,2,3]


# In[64]:


newdf.head()


# In[65]:


newdff.head()


# In[66]:


con=pd.concat([newdf, newdff])


# In[67]:


con


# In[68]:


dff= pd.DataFrame({"name": ['NaN', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})


# In[69]:


dff.to_csv('dff1', index=False)


# In[70]:


dff1=pd.read_csv('dff1')


# In[71]:


dff1


# In[72]:


dff1['name'].isnull


# In[73]:


dff1.dropna(how='all')


# In[ ]:





# In[ ]:




