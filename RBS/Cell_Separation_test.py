
# coding: utf-8

# Importing libraries

import pandas as pd
import numpy as np
import re

# Reading of a input file

prac = pd.read_csv("C:\\Users\\Manish411\\Desktop\\practice.csv",header=0)

# Checking the dimension of the input file

prac.shape

# In[37]:

data = prac

# In[38]:

data

# In[39]:

d1 = data["Data1"]
d1

# In[40]:

d2 = d1[0]

# In[41]:

d2 = d2.splitlines()

# In[42]:

d2 = [x.strip(' ') for x in d2]

# In[43]:

d2
#type(d2)

# In[44]:

l1 = []
for char in d2:
    lst = char[:3]
    l1.append(lst)
    
print(l1)

# In[45]:

from collections import Counter, defaultdict

def duplicates(lst):
    cnt= Counter(lst)
    return [key for key in cnt.keys() if cnt[key]> 1]

def duplicates_indices(lst):
    dup, ind= duplicates(lst), defaultdict(list)
    for i, v in enumerate(lst):
        if v in dup: ind[v].append(i)
    return ind


# In[46]:

print(duplicates(l1))
print(duplicates_indices(l1))

# In[47]:

k = duplicates_indices(l1)
print(k.keys())
k.values()

# In[48]:

exclude_index = [value[0] for key,value in k.items() if re.match('^[0-9][a-z]\.',key)]
exclude_index

# In[49]:

d2 =[i for j,i in enumerate(d2) if j not in exclude_index]

# In[50]:

d3 = [i for i in d2 if re.match('(^[0-9][a-z]\..*\?$)',i) is None]
d3

# In[52]:

d3 = [x for x in d3 if x != '']
d3

# In[59]:

d4 = '\n'.join(d3)
d4

