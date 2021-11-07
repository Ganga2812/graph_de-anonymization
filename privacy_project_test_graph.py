#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import math
import statistics


# In[2]:


G1 = nx.Graph()

#This graph is based on the one from the powerpoint/pdf CH6

G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
G1.add_node(5)
G1.add_node(6)
G1.add_node(7)

G1.add_edge(0, 1)
G1.add_edge(0, 5)
G1.add_edge(1, 4)
G1.add_edge(1, 5)
G1.add_edge(1, 6)
G1.add_edge(1, 7)
G1.add_edge(2, 5)
G1.add_edge(2, 6)
G1.add_edge(3, 6)

print(nx.info(G1))


# In[3]:


G2 = nx.Graph()

#This graph is based on the one from the powerpoint/pdf CH6

G2.add_node(0)
G2.add_node(1)
G2.add_node(2)
G2.add_node(3)
G2.add_node(4)
G2.add_node(5)
G2.add_node(6)

G2.add_edge(0, 5)
G2.add_edge(0, 6)
G2.add_edge(1, 2)
G2.add_edge(1, 4)
G2.add_edge(1, 5)
G2.add_edge(2, 3)
G2.add_edge(2, 4)
G2.add_edge(4, 5)

print(nx.info(G2))


# In[4]:


arrayG1 = list(nx.nodes(G1))
arrayG2 = list(nx.nodes(G2))
seedPairG1 = [0, 5, 6]
seedPairG2 = [6, 5, 4]
nonMatchedG1 = [x for x in arrayG1 if (x not in seedPairG1)]
nonMatchedG2 = [x for x in arrayG2 if (x not in seedPairG2)]


# In[5]:


for x in nonMatchedG1:
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
    print("Node V =", x)
    print("Scores =", scoreList)
    print("Std =", std)
    print("Max1 =", max1)
    print("Max2 =", max2)
    print("ECCE = (", max1, "-", max2, ") /", std, "=", ecce)
    print("ECCE =", ecce)
    #We now have the ecce.
    #But what's the threshold? If ecce > threshold match node V (y) and U (x).
    print(" ")
    print("-----")
    print(" ")


# In[ ]:




