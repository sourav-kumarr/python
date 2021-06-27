#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Program to Illustrate Different Set Operations
l0={1,2,3,4}
l3={3,4,5,6}
x=l0.union(l3)
print(x)
y=l0.intersection(l3)
print(y)
z=l0.difference(l3)
print(z)


# In[8]:


# Joining Two Sets
l0.update(l3)
print(l0)


# In[ ]:




