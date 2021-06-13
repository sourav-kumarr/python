#!/usr/bin/env python
# coding: utf-8

# In[5]:


celsius=float(input("temperature in celsius:"))
fahrenhiet=(celsius*1.8)+32
print("%.2f c= %.2f f" %(celsius,fahrenhiet))


# In[6]:


kilometer=float(input("distance in kilometer:"))
mile=kilometer*0.621
print("%.2f k=%.2f m" %(kilometer,mile))


# In[18]:


number=int(input("enter the number:"))
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")


# In[20]:


number=int(input("enter the number"))
if number>0:
    print("the number is postive")
elif number<0:
    print("the number is negtive")
else:
    print("the number is zero")


# In[41]:


year=int(input("enter a year:"))
if(year%4)==0: 
    if(year%100)==0:
        if(year%400)==0:
            print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[42]:


first=int(input("enter the first number:"))
second=int(input("enter the second number"))
third=int(input("enter the third number"))
if first>second>third:
    print(first,"number is larger")
elif second>first>third:
    print(second,"number is larger")
else:
    print(third,"number is larger")


# In[45]:


number=int(input("enter a number:"))
for i in range(2,number):
    if number%i==0:
        print(number, "is not an prime number")
else:
    print(number,"is an prime number ")


# In[65]:


lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit"))
print("the prime number between",lower, "and",upper," are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                
                break;
                    
        else:
            print(num,"these are  prime numbers")
    


# In[15]:


number=int(input("enter the number:"))
factorial=1
if number<0:
    print("the factorial of a negative number doesnt exist")
elif number==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("the facrorial of the",number,"is",factorial)


# In[10]:


number=int(input("enter a number:"))
for i in range(1,11):
    
    print(number,"x",i,"=",number*i)


# In[ ]:





# In[ ]:




