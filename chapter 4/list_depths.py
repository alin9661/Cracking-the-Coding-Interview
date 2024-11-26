'''
4.3 List of Depths: Given a binary tree, design an algorithm which creates 
    a linked list of all the nodes at each depth (e.g., if you have a tree 
    with depth D, you'll have D linked lists).
'''
from typing import List

class Node:
    def __init__(self, num):
        self.data = None | num
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.list: List[Node] = None

class BinaryTree:
    class BinaryNode:
        def __init__(self, num):
            self.data = None | num
            self.left = None
            self.right = None

    def list_depths(self, ):