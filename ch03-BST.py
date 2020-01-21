#!/usr/bin/env python
# coding: utf-8

# BST.
# 
# Better than O(n) search and better than O(n) update.
# 
# Basic BST operations: search, insert, delete and traverse.
# 
# 

# In[ ]:


from __future__ import annotations
from typing import List, TypeVar, Tuple

V = TypeVar('V')

class BST_Node:
    """A BST tree node"""
    def __init__(self, data: V):
        self.data = data
        self.left: BST_Node = None
        self.right: BST_Node = None
        self.parent: BST_Node = None



def BST_search(root: BST_Node, data: V) -> BST_Node:
    """O(h) time where h is the height of the tree
       Returns the node found and its parent
       Note: parent is None for the tree's root node
    """
    if root is None:
        return None
    
    if data == root.data:
        return root
    
    if data > root.data:
        return BST_search(root.right, data)
    
    if data < root.data:
        return BST_search(root.left, data)


def BST_traverse(root: BST_Node, order: str) -> List[BST_Node]:
    return tree_traverse(root, order)

def tree_traverse(root: BST_Node, order: str):
    """Traverse a binary tree. O(n) time.  Each node is visited exactly once.
       order = 'in', 'pre', or 'post'
    """
    if root is None:
        return None
    
    nodes_left = []
    if root.left is not None:
        nodes_left = tree_traverse(root.left, order)
        
    nodes_right = []    
    if root.right is not None:
        nodes_right = tree_traverse(root.right, order)

    return {
        'in': lambda: nodes_left + [root] + nodes_right,
        'pre': lambda: [root] + nodes_left + nodes_right,
        'post': lambda: nodes_left + nodes_right + [root],
    }.get(order, lambda: None)()

        
def BST_find_max(root: BST_Node) -> BST_Node:
    """Return node with max data.  O(h) time where h is the height of the tree"""
    if root is None:
        return None

    node = root
    while node.right is not None:
        node = node.right
    return node

def BST_find_min(root: BST_Node) -> BST_Node:
    """Return node with min data.  O(h) time where h is the height of the tree"""
    if root is None:
        return None

    node = root
    while node.left is not None:
        node = node.left
    return node

def BST_print(root_node: BST_Node):
    nodes = BST_traverse(root_node, 'in')
    in_order_data_list = []
    for node in nodes:
        in_order_data_list.append(node.data)

    print(in_order_data_list)
    print("\nNode:Parent:Left:Right")
    for n in nodes:
        d_n, p_n, l_n, r_n = 0, 0, 0, 0
        d_n = n.data
        if n.parent:
            p_n = n.parent.data
        if n.left:
            l_n = n.left.data
        if n.right:
            r_n = n.right.data
        print(f'{d_n}:{p_n}:{l_n}:{r_n}')


# Insert a node into a BST tree at a leaf location where it should have been found.

# In[ ]:


def BST_insert(root: BST_Node, node_data: V):
    if root is None:
        return
    
    if node_data == root.data: # node found, redundant
        return

    if node_data > root.data: # going down the right subtree
        
        if root.right is None:
            node = BST_Node(node_data)
            node.parent = root
            root.right = node
        else:
            BST_insert(root.right, node_data)
            
    else: # going down the left subtree
        
        if root.left is None:
            node = BST_Node(node_data)
            node.parent = root
            root.left = node
        else:
            BST_insert(root.left, node_data)
    


# Deleting a node in a BST:
# 
# If the node is a leaf node, adjust the pointer of its parent.
# 
# If the node has only one child, link its child to the "grand-parent".
# 
# If the node has two children, move the smallest node in the parent's right subtree to its place. This is essentially the left most element of the right subtree.

# In[ ]:


def BST_inherit_child(parent: BST_Node, child: BST_Node) -> None:
    if parent.data > child.data:
        parent.left = child
    else:
        parent.right = child
    child.parent = parent
    
def BST_delete(root: BST_Node, node_data: V) -> bool:
    """Return True if the node is found and deleted
              False otherwise
    """
    # search the node, if not found, return False
    node = BST_search(root, node_data) 
    if node is None: 
        return False
    
    # node is a leaf, pick it off
    if node.left is None and node.right is None: 
        if node.parent.data > node.data:
            node.parent.left = None
        else:
            node.parent.right = None
        return True
        
    # node has only one child in the two cases below
    # let the grand parent inherit the child
    if node.left is not None and node.right is None:
        BST_inherit_child(node.parent, node.left)
        return True
        
    if node.right is not None and node.left is None:
        BST_inherit_child(node.parent, node.right)
        return True
    
    # node has two children
    # replace the node with the smallest node in the right subtree
    assert (node.right is not None and node.left is not None)
    smallest = BST_find_min(node.right)
    
    if smallest.parent.data > smallest.data:
        smallest.parent.left = None
    else:
        smallest.parent.right = None
        
    smallest.left = node.left
    smallest.right = node.right
    BST_inherit_child(node.parent, smallest)
    
    return True


# Test cases ...

# In[117]:


if name == "main":


# In[116]:


"""insert Test 1, build a BST using BST_insert() with node data
    node_data[0] is the root node.
"""

#node_data = [50, 35, 90, 32, 40, 25, 70, 55, 60, 30, 20, 10, 80, 75, 65]

node_data = [50, 40, 70, 30, 60, 80, 90, 70, 10, 20]

root_node = BST_Node(node_data[0])

for i in range(1, len(node_data)):
    BST_insert(root_node, node_data[i])
print("\nA tree is created:\n")
BST_print(root_node)

"""insert Test 2, insert nodes by value"""
print("\nInserting 35\n")
BST_insert(root_node, 35)
BST_print(root_node)

print("\nInserting 77\n")
BST_insert(root_node, 77)
BST_print(root_node)

print("\nInserting 85\n")
BST_insert(root_node, 85)
BST_print(root_node)

print("\nInserting 105\n")
BST_insert(root_node, 105)
BST_print(root_node)


"""insert Test 3, insert a subtree"""

"""delete Test case 1, deleting a leaf node"""
print("\nDeleting a leaf node (35)\n")
BST_delete(root_node, 35)
BST_print(root_node)

"""delete Test case 2, deleting a node that has only one child"""
print("\nDeleting a node with one child (10)\n")
BST_delete(root_node, 10)
BST_print(root_node)

"""delete Test case 3, deleting a node with 2 children"""
print("\nDeleting a node with 2 children (70)\n")
BST_delete(root_node, 70)
BST_print(root_node)

"""delete Test case 4, deleting a node with 2 children"""
print("\nDeleting a node with 2 children (90)\n")
BST_delete(root_node, 90)
BST_print(root_node)

"""delete Test case 5, deleting a non-existing node"""
print("\nDeleting a non-existent node 101010\n")
deleted = BST_delete(root_node, 101010)
if deleted is False:
    print(f'-->> Node 101010 does not exist! (Success)')


# In[ ]:




