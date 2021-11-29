from bst_methods import *
from avltree import AVLTree


def insertion_unit_test():
    
    my_avl = AVLTree()
    insertions = [10, 20, 30, 40, 50, 25]
    for i in insertions:
        my_avl.root = my_avl.insert(i)

    print("Preorder traversal of the constructed AVL tree is")
    pre_order(my_avl.root)
    print()
    print("Should be : 30 20 10 25 40 50 ")
    
def deletion_unit_test():
    my_avl = AVLTree()
    insertions = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for i in insertions:
        my_avl.insert(i)

    print("Preorder traversal of the constructed AVL tree is")
    pre_order(my_avl.root)
    print()

    elm = 10
    my_avl.delete(elm)
    
    print("Preorder traversal post deletion")
    pre_order(my_avl.root)
    print()
    print("1 0 -1 9 5 2 6 11")

def find_unit_test():
    my_avl = AVLTree()
    insertions = [10, 20, 30, 40, 50, 25]
    for i in insertions:
        my_avl.root = my_avl.insert(i)
    
    for i in insertions:
        print(f"There is {i} : {find(my_avl.root, i)} ")
    i = 100
    print(f"There is {i} : {find(my_avl.root, i)} ")

def bst_test():
    insertions = [20, 30, 10, 25, 35, 5]
    root = None
    for i in insertions:
        root = insert(root, i, node_type="BSTNode")
    in_order(root)
    print()

def node_name(node):
    s = str(node.__class__).strip("<>'")
    return s[ s.rfind(".")+1 :]

if __name__ == '__main__':
    # insertion_unit_test()
    deletion_unit_test()
