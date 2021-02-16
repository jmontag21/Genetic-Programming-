#!/usr/bin/env python
# coding: utf-8

import operator
import math
import random
import math
import pygraphviz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
import networkx as nx


# In[275]:


#split into train and testing data
df = pd.read_csv('SPY.csv' ,index_col = 'Date', parse_dates = True)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
train = df.loc['2000-1-1' : '2003-1-1']
test = df.loc['2004-1-1' : '2005-1-1']
test.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
train.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
train.head()


# In[276]:




pset = gp.PrimitiveSetTyped('MAIN', [float],float)

pset.renameArguments(ARG0='adj_close')



# In[277]:
def add(left, right):
    return left + right
    
def subtract(left, right):
    return left - right
      
def multiply(left, right):
    return left * right

def divide(left, right):
    return left / right


#Addition
pset.addPrimitive(add,  [float, float], float, name="Add")

#Subtraction
pset.addPrimitive(subtract ,[float, float], float, name="Sub")

#Multiplication
pset.addPrimitive(multiply,  [float, float], float, name="Mul")

#Division
pset.addPrimitive(divide,  [float, float], float, name="Div")


# In[278]:


creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', gp.PrimitiveTree, fitness=creator.FitnessMax)


# In[279]:


toolbox = base.Toolbox()
toolbox.register('expr', gp.genHalfAndHalf, pset=pset, min_=1, max_=6)
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('compile', gp.compile, pset=pset)


# In[280]:


def evalFitness(individual, points):
    return .5,


# In[281]:


toolbox.register('evaluate', evalFitness, points=train)
toolbox.register('select', tools.selTournament, tournsize=3)
toolbox.register('mate', gp.cxOnePoint)
toolbox.register('expr_mut', gp.genFull, min_=0, max_=3)
toolbox.register('mutate', gp.mutUniform, expr=toolbox.expr_mut, pset=pset)


# In[284]:


def plot(individual):
    nodes, edges, labels = gp.graph(individual)
    plt.figure(figsize=(12,7))
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    pos = nx.drawing.nx_agraph.graphviz_layout(g, prog="dot")
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos, labels)
     
    nx.draw(g,pos)
    plt.show()

# In[285]:


pop = toolbox.population(n=200)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register('avg', np.mean)
stats.register('min', np.min)
stats.register('max', np.max)
pop, log = algorithms.eaMuPlusLambda(pop, toolbox, 160, 160, 0.6, 0.1, 50, stats=stats, halloffame=hof)
# get the info of best solution
print("Best solution found...")
print(hof[0])
plot(hof[0])
f=toolbox.compile(hof[0])



