#!/usr/bin/env python
# coding: utf-8

# In[8]:


from difflib import SequenceMatcher

# Store the file
filename = 'document.txt'
sen = []

# Store in the data
f = open(filename)
data = f.readlines()
f.close()

# Split the sentence
for n, line in enumerate(data, 1):
    sen.append(line)

# Check the length
lent=len(sen)

# Check for similarity
for i in range(0, lent):
    for j, val in enumerate(sen):
        while i == j :
            break
        else :
            #print(i, j)
            b = SequenceMatcher(None, sen[i], sen[j]).ratio()
            thr = 0.95 # threshold is 95 % Threshold can be changed
            if b > thr:
                print(i, j)
                print(b)
                print(sen[i])
                print(sen[j])
                print('--------------------------------')


# In[ ]:




