#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Q1
l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
print(l)
l.sort(key=lambda x:x)
print(l)


# In[14]:


#Q2
numbers = [1,2,3,4,5,6,7,8,9,10]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))


# In[17]:


#Q3
numbers = [1,2,3,4,5,6,7,8,9,10]
strtup = map(lambda x: str(x), numbers)
print(tuple(strtup))


# In[26]:


#Q4
from functools import reduce
n=[]
for i in range(1,26,1):
    n.append(i)
print(n)
product = reduce(lambda x, y: x*y, n)
print(product)


# In[43]:


#Q5
numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
div = filter(lambda x: x if (x%2==0 or x%3==0) else None , numbers)
print(list(div))


# In[44]:


#Q6
texts = ['python', 'php', 'aba', 'radar', 'level']
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print(result) 

