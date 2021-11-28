from math import log10, log2
from itertools import accumulate
from operator import mul
from typing import List


class Node:
    def __init__(self, _data:int, _height:int=1) -> None:
        self.data = _data
        self.height = _height
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, key) -> Node: 
        if root == None:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        
        update_height(root)

        b_factor = balance_factor(root)
        if abs(b_factor) <= 1:
            return root

        if b_factor > 1:
            if key < root.left.data: # Left-Left Case
                return self.right_rotate(root)
            elif key > root.left.data: # Left-Right Case z(this node) > w(newly inserted) > x(z's grand-child) > y(z's child)
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif b_factor < -1: # Right-Right
            if key > root.right.data:
                return self.left_rotate(root)
            elif key < root.right.data: # Right-Left key < root.right.val
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

    def right_rotate(self, root)->Node:
        left_child = root.left

        root.left = left_child.right # since child is on the left of the current node which is the first node with the imbalance
        left_child.right = root

        update_height(root)# = 1 + max(root.right.height, root.left.height)
        update_height(left_child)# = 1 + max(left_child.right.height, left_child.left.height)

        return left_child

    def left_rotate(self, root)->Node:
        right_child = root.right

        root.right = right_child.left  # since child is on the right of the current node
        right_child.left = root

        update_height(root)# = 1 + max(root.right.height, root.left.height)
        update_height(right_child)# = 1 + max(right_child.right.height, right_child.left.height)

        return right_child

    def pre_order(self, root):
        if not root:
            return
 
        print("{0} ".format(root.data), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

def get_height(node:Node)->int:
    if not node:
        return 0
    return node.height

# If balance factor is greater than 1, then the current node is unbalanced and we are either in Left Left case or left Right case. 
# To check whether it is left left case or not, compare the newly inserted key with the key in left subtree root. 
# If balance factor is less than -1, then the current node is unbalanced and we are either in Right Right case or Right-Left 
# case. To check whether it is Right Right case or not, compare the newly inserted key with the key in right subtree root. 
def balance_factor(node:Node)->int:
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right) # with the minus sign, I have a sense of direction now


def update_height(node:Node):
    if node:
        node.height = 1 + max( get_height(node.left), get_height(node.right) )

def find(root:Node, val:int):   
    if root == None:
        return False
    elif root.data == val:
        return True
    elif root.data < val:
        return find(root.right, val)
    elif root.data > val:
        return find(root.left, val)


def unit_test():
    my_avl = AVLTree()
    insertions = [10, 20, 30, 40, 50, 25]
    for i in insertions:
        my_avl.root = my_avl.insert(my_avl.root, i)

    print("Preorder traversal of the constructed AVL tree is")
    my_avl.pre_order(my_avl.root)
    print()
    print("Should be : 30 20 10 25 40 50 ")
    
    for i in insertions:
        print(f"There is {i} : {find(my_avl.root, i)} ")
    i = 100
    print(f"There is {i} : {find(my_avl.root, i)} ")

unit_test()
