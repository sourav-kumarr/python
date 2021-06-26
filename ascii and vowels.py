#!/usr/bin/env python
# coding: utf-8

# In[1]:


character=input("enter a letter:")
print(f"ASCII value of {character} : " ,ord(character))


# In[2]:


# to count number of vowels in a word
word=input("enter any word:")
vowel_count=0
for i in word:
    if i in ['a','e','i','o','u']:
        vowel_count+=1

print("There are %s Vowels in %s " %(vowel_count,word))


# In[ ]:




