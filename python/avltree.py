from math import log10, log2
from itertools import accumulate
from operator import mul
from typing import List


class Node:
    def __init__(self, _val:int, _height:int=0) -> None:
        self.val = _val
        self.height = _height
        self.left = None
        self.right = None



def check_balance(node:Node)->int:
    if node != None:
        return node.left.height - node.right.height
    return -1 # not sure about this


def find(root:Node, val:int):
    pass
