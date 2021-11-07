#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import math
import statistics


# In[2]:


data_dir1 = r'C:\Users\Dan\(2) privacy\part1\\'
file1 = 'seed_G1.edgelist'

data_dir2 = r'C:\Users\Dan\(2) privacy\part1\\'
file2 = 'seed_G2.edgelist'

data_dir3 = r'C:\Users\Dan\(2) privacy\part1\\'
file3 = 'seed_node_pairs.txt'


# In[3]:


G1 = nx.read_edgelist(data_dir1+file1, create_using=nx.Graph(), nodetype=int)

G2 = nx.read_edgelist(data_dir2+file2, create_using=nx.Graph(), nodetype=int)

print(nx.info(G1))
print("")
print(nx.info(G2))

arrayOfNodesG1 = list(nx.nodes(G1))

arrayOfNodesG2 = list(nx.nodes(G2))

seedPairG1 = []
seedPairG2 = []

with open(data_dir3+file3, "r") as text_file:
    for line in text_file:
        line = line.strip()
        number1 , number2 = line.split(" ")
        seedPairG1.append(int(number1))
        seedPairG2.append(int(number2))
        
unMatched = [x for x in arrayOfNodesG2 if (x not in seedPairG2)]


# In[4]:


def calc(arrayG1:list, arrayG2:list, nonMatchedG2:list):
    for x in range(len(arrayG1)):
        scoreList = []
        degreeOfV = len(list(nx.neighbors(G1, x)))
        for y in nonMatchedG2:
            count = 0
            degreeOfU = len(list(nx.neighbors(G2, y)))
            neighbors = list(nx.neighbors(G2, y))
            for nodeU in neighbors:
                for z in seedPairG2:
                    if nodeU == z:
                        count = count + 1
            score = (count)/(math.sqrt(degreeOfV) * math.sqrt(degreeOfU))
            scoreList.append(score)
        std = statistics.pstdev(scoreList)
        max1 = max(scoreList)
        scoreList.remove(max1)
        max2 = max(scoreList)
        ecce = (max1 - max2)/(std)
        #print("Node V =", x)
        #print("Scores =", scoreList)
        #print("Std =", std)
        #print("Max1 =", max1)
        #print("Max2 =", max2)
        #print("ECCE = (", max1, "-", max2, ") /", std, "=", ecce)
        print("ECCE =", ecce)
        #We now have the ecce.
        #But what's the threshold? If ecce > threshold match node V (y) and U (x).
        print(" ")
        print("-----")
        print(" ")
    pass


# In[ ]:


calc(arrayOfNodesG1, arrayOfNodesG2, unMatched)


# In[ ]:




