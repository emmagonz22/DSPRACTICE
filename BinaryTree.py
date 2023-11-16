## This document is a practice of the Binary Tree implementation and variants 
# Binary Tree

class BinaryTreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    



class BinaryTree:

    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def in_order_traversal(self, root):
        if not root:
            return
       
        self.in_order_traversal(root.left)
        print(root.value)
        self.in_order_traversal(root.right)


    def pre_order_traversal(self):
        if not root:
            return
        print(root.value)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def post_order_traversal(self):
        if not root:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.value)

    def insert(self, value):
        pass

    def get_height(self):
        pass

    def get_depth(self):
        pass
    
# Heap (List implementation)
class MinHeap: 
    # Time Complxity
    # Add    O(logn)
    # Remove O(1)
    # Heapify

    # Parent Node   (i-1)/2
    # Right Child   (i+1)/2
    # Left Child
    def __init__(): #
        pass 

    def extract_min(self):
        pass 

    def insert(self): # O(logn)
        pass

    def heapify(self):
        pass

class MaxHeap:
    # Time Complxity
    # Add    O(logn)
    # Remove O(1)
    # Heapify

    # Parent Node   (i-1)/2
    # Right Child   (i+1)/2
    # Left Child

    def __init__():
        pass 


    def extract_max(self):
        pass

    def insert(self): # O(logn)
        pass

    def heapify(self):
        pass

# BST 

class BST:
    def __init__(self):
        self.root = root
        


    






   


# 


