#!/usr/bin/env python
# coding: utf-8

# In[1]:


#gcd or hcf of two numbers
def gcd(num1,num2):
    if num2==0:
        return num1
    else:
        return gcd(num2, num1%num2)
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num=gcd(num1,num2)
print("GCD of two number is:")
print(num)


# In[ ]:




