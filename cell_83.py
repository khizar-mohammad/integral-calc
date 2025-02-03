#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Enter the number to generate it's integral dictionary")
x = int(input())
myDict = {}
for i in range(1,x+1,1):
  myDict[i] = i*i

print(myDict)

