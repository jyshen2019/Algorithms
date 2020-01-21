#!/usr/bin/env python
# coding: utf-8

# Lists and Arrays.
# 
# Both are recursive objects.  
# 
#     Choppping off the first element in a list leaves a smaller list.  Same is the case with string of characters.
# 
#     Splitting an array leaves two small arrays.
#     
# Simpler list processing, divide-and-conquer algorithms, and binary searches are nicely facilitated by this recursive property of arrays and lists.
# 
# 

# Containers are data structures where content of the data structure is independent of the storage and retrieval of the data.  Stack and Queues are containers.
# 
# Dictionaries, on the other hand are abstract data type that retrieve based on key values or content.

# Stacks vs. Queues, LIFO vs. FIFO, and DFS vs. BFS.

# Dictionaries.
# 
# Insert/add to a dictionary:

# In[ ]:


dd = {'a': 1, 'b': 2, 'c': 3}

print(dd)

dd['d'] = 4

print(dd)


# deleting a data item in a dictionary:

# In[ ]:


del dd['d']

print(dd)


# or ...

# In[ ]:


dd.pop('c')

print(dd)


# Retrieve the item with the largest and smallest keys ...

# In[ ]:


dd['c'] = 3

dd['d'] = 4

dd['z'] = 26

print(dd)

print(dd[max(dd)]) # returns largest key's value

print(dd[min(dd)]) # returns smallest key's value


# Presenting dictionary data items in sorted order:

# In[ ]:


d1 = {'b': 2,'z': 26, 'c': 3, 'd': 4, 'a': 1, 'u': 10}

sk = sorted(d1) # sorted returns sorted d1.keys()

d2 = {}
for k in sk:
    d2[k] = d1[k]

print(d1)

print(d2)
    


# Dictionary implementation:
#     
# Sorted array or unsorted array
# Singly linked list, sorted or unsorted
# Doubly linked list, sorted or unsorted
# 
# What are asymptotic worst-case running time in big O notation of each of the 7 dictionary operations?
# - Search
# - Insert
# - Delete
# - Traverse: Successor
# - Traverse: Predecessor
# - Maximum
# - Minimum
# 
# Each has its advantages for certain operations.  So when seleting implementation, pick the one that matters for the most common operations for the dictionary in questiom.
# 
# Fast search vs. fast update.
# 

# BST.
