from typing import Any, Callable, Optional

class BSTNode:
    def __init__(self, _data:int) -> None:
        self.data = _data
        self.left : Optional[BSTNode] = None
        self.right : Optional[BSTNode] = None

def node_name(node):
    s = str(node.__class__).strip("<>'")
    return s[ s.rfind(".")+1 :]

def get_class( kls:str )->Any:
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

def find(root:Optional[BSTNode], val:int)->bool:
    if root is None:
        return False
    elif root.data == val:
        return True
    elif root.data < val:
        return find(root.right, val)
    elif root.data > val:
        return find(root.left, val)

def find_min(root:Optional[BSTNode])->Optional[BSTNode]:
    if root is None or root.left is None:
        return root
    return find_min(root.left)

def find_max(root:Optional[BSTNode])->Optional[BSTNode]:
    if root is None or root.right is None:
        return root
    return find_max(root.right)

def insert( root:Optional[BSTNode],
            key:int,
            further_enhancing_methods : Optional[Callable] = None,
            node_type : Optional[str] = None)->Optional[BSTNode]:
        if root is None:
            node = get_class(node_type)
            return node(key)
        elif key < root.data:
            root.left = insert(root.left, key, further_enhancing_methods, node_type)
        elif key > root.data:
            root.right = insert(root.right, key, further_enhancing_methods, node_type)

        if further_enhancing_methods:
            root = further_enhancing_methods(root, key)

        return root

def delete( root:Optional[BSTNode],
            key:int,
            further_enhancing_methods : Optional[Callable] = None,
            ) -> Optional[BSTNode]:
    if root is None:
        return root
    elif key < root.data:
        root.left = delete(root.left, key, further_enhancing_methods)
    elif key > root.data:
        root.right = delete(root.right, key, further_enhancing_methods)
    else:
        if root.left is None: # root is the smallest in this subtree
            t = root.right
            root = None
            return t
        elif root.right is None: # root is the biggest in this subtree
            t = root.left
            root = None
            return t

        t = find_min(root.right)
        root.data = t.data
        root.right = delete(root.right, t.data, further_enhancing_methods)

    if root is None:
        return root

    if further_enhancing_methods:
        root = further_enhancing_methods(root)

    return root


def pre_order(root:Optional[BSTNode]):
        if root is None:
            return

        print("{0} ".format(root.data), end="")
        pre_order(root.left)
        pre_order(root.right)

def in_order(root:Optional[BSTNode]):
        if root is None:
            return

        in_order(root.left)
        print("{0} ".format(root.data), end="")
        in_order(root.right)
