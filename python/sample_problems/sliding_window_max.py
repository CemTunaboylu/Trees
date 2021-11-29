from os import path
from sys import path as sys_path

from typing import List
sys_path.append( path.abspath( path.join( path.pardir, "" ) ) )

from avltree import AVLTree
from bst_methods import find_max

def max_sliding_window(arr: List[int], K) -> List[int]:
    avl = AVLTree()
    res = []

    b = len(arr) - K

    for num in arr[:K]:
        avl.insert(num)
    
    for i in range(0,b):
        res.append( find_max(avl.root).data )
        avl.delete(arr[i])
        avl.insert(arr[K+i])

    res.append( find_max(avl.root).data )
    return  res

def unit_test_1():
    arr, K = [1, 2, 3, 1, 4, 5, 2, 3, 6], 3
    res = max_sliding_window(arr, K)
    assert [3, 3, 4, 5, 5, 5, 6] == res


def unit_test_2():
    size = 100_000
    arr = list(range(size))
    K = 10
    res = max_sliding_window(arr, K)
    cor = list(range(K-1, size))
    assert cor == res

def unit_test_3():
    size = 11
    arr, K = list(range(1,size)), 3
    res = max_sliding_window(arr, K)
    cor = list(range(K, size))
    assert cor == res

def unit_test_4():
    arr, K = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4
    res = max_sliding_window(arr, K)
    cor = [10, 10, 10, 15, 15, 90, 90]
    assert cor == res


if __name__ == '__main__':
    unit_test_1()
    unit_test_2()
    unit_test_3()
    unit_test_4()