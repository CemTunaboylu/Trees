from itertools import accumulate
from typing import List

from bst_methods import *

class AVLNode(BSTNode):
    def __init__(self, _data:int, _height:int=1) -> None:
        super().__init__(_data)
        self.height = _height

def get_height(node:AVLNode)->int:
    if node is None:
        return 0
    return node.height

def balance_factor(node:AVLNode)->int:
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right) # with the minus sign, I have a sense of direction now

def update_height(node:AVLNode):
    if node:
        node.height = 1 + max( get_height(node.left), get_height(node.right) )

class AVLTree:
    def __init__(self) -> None:
        self.root = None
        self.node_type = "avltree.AVLNode" #this is bad find a fix

    def insert(self, key): 
        self.root = insert(self.root, key, avl_property_insertion, self.node_type)

    def delete(self, key):
        self.root = delete(self.root, key, avl_property_deletion)
        
def avl_property_insertion(root, key) -> AVLNode:
    update_height(root)

    b_factor = balance_factor(root)
    if abs(b_factor) <= 1:
        return root

    if b_factor > 1:
        if key < root.left.data: # Left-Left Case
            return right_rotate(root)
        elif key > root.left.data: # Left-Right Case z(this node) > w(newly inserted) > x(z's grand-child) > y(z's child)
            root.left = left_rotate(root.left)
            return right_rotate(root)
    elif b_factor < -1: # Right-Right
        if key > root.right.data:
            return left_rotate(root)
        elif key < root.right.data: # Right-Left key < root.right.val
            root.right = right_rotate(root.right)
            return left_rotate(root)

def avl_property_deletion(root) -> AVLNode:
    
    update_height(root)

    b_factor = balance_factor(root)
    if abs(b_factor) <= 1:
        return root

    elif b_factor > 1:
        l_balance = balance_factor(root.left)
        if l_balance >= 0: # Left-Left Case -> left subtree has greater height
            return right_rotate(root)
        else: # Left-Right Case -> right subtree has greater height 
            root.left = left_rotate(root.left)
            return right_rotate(root)
    elif b_factor < 1:
        r_balance = balance_factor(root.right)
        if r_balance <= 0:# Right-Right Case -> right subtree has greater height
            return left_rotate(root)
        else: #Right-Left Case -> left subtree has greater height
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def right_rotate(root)->AVLNode:
    left_child = root.left

    root.left = left_child.right # since child is on the left of the current node which is the first node with the imbalance
    left_child.right = root

    update_height(root)# = 1 + max(root.right.height, root.left.height)
    update_height(left_child)# = 1 + max(left_child.right.height, left_child.left.height)

    return left_child

def left_rotate(root)->AVLNode:
    right_child = root.right

    root.right = right_child.left  # since child is on the right of the current node
    right_child.left = root

    update_height(root)# = 1 + max(root.right.height, root.left.height)
    update_height(right_child)# = 1 + max(right_child.right.height, right_child.left.height)

    return right_child
