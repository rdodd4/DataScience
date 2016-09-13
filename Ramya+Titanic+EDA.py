
# coding: utf-8

# In[1]:

import pandas as pd
get_ipython().magic(u'pylab inline')


# In[2]:

df=pd.read_csv("train.csv")


# In[3]:

df


# In[4]:

df.PassengerId.value_counts()


# In[5]:

df.describe()


# In[6]:

df(df.PassengerId.isnull())


# In[7]:

df(df.PassengerId.isnull())


# In[8]:

df[df.PassengerId.isnul()]


# In[9]:

df[df.PassengerId.isnull()]


# In[10]:

df.PassengerId.hist()


# In[11]:

df.PassengerId.value_counts().plot(kind='bar')


# In[12]:

df.Survived.value_counts()


# In[13]:

df[df.Survived.isnull()]


# In[14]:

df.describe()


# In[15]:

df.Survived.hist()


# In[16]:

df.Pclass.value_counts()


# In[17]:

df[df.Pclass.isnull()]


# In[18]:

df.describe()


# In[19]:

df.Pclass.hist()


# In[20]:

df.Sex.value_counts()


# In[21]:

df[df.Sex.isnull()]


# In[22]:

df.describe()


# In[23]:

df.Sex.hist()


# In[24]:

df.Sex.hist()


# In[25]:

df.Sex.value_counts().plot(kind='bar')


# In[26]:

df.Age.value_counts()


# In[27]:

df[df.Age.isnull()]


# In[28]:

df.describe()


# In[29]:

df.Age.hist()


# In[30]:

df.SibSp.value_counts()


# In[31]:

df[df.SibSp.isnull()]


# In[32]:

df.describe()


# In[33]:

df.SibSp.hist()


# In[34]:

df.Parch.value_counts()


# In[35]:

df[df.Parch.isnull()]


# In[36]:

df.describe()


# In[37]:

df.Parch.hist()


# In[38]:

df.Ticket.value_counts()


# In[39]:

df[df.Ticket.isnull()]


# In[40]:

df.describe()


# In[41]:

df.Ticket.hist()


# In[43]:

df.Ticket.value_counts().plot(kind='bar')


# In[44]:

df.Fare.value_counts()


# In[45]:

df[df.Fare.isnull()]


# In[46]:

df.Fare.hist()


# In[47]:

df.describe()


# In[48]:

df.Cabin.value_counts()


# In[49]:

df[df.Cabin.isnull()]


# In[50]:

df.describe()


# In[51]:

df.Cabin.hist()


# In[52]:

df.Cabin.value_counts().plot(kind='bar')


# In[53]:

df.Embarked.value_counts()


# In[54]:

df[df.Embarked.isnull()]


# In[55]:

df.describe()


# In[56]:

df.Embarked.hist()


# In[57]:

df.Embarked.value_counts().plot(kind='bar')


# In[ ]:



