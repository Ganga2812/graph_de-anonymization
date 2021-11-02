#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
#you can leave these alone


# In[2]:


data_dir1 = r'C:\Users\Dan\(0) privacy\part1\\' #you might need to change to your directory
file1 = 'seed_G1.edgelist' #you don't need to change this


# In[3]:


a = nx.read_edgelist(data_dir1+file1, create_using=nx.Graph(), nodetype=int)

print(nx.info(a))

nx.draw(a)

plt.show()


# In[4]:


data_dir2 = r'C:\Users\Dan\(0) privacy\part1\\' #you might need to change to your directory
file2 = 'seed_G2.edgelist' #you don't need to change this


# In[5]:


b = nx.read_edgelist(data_dir2+file2, create_using=nx.Graph(), nodetype=int)

print(nx.info(b))

nx.draw(b)

plt.show()


# In[ ]:




