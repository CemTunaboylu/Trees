# Trees
Code + algorithms on various tree data structures.

### Typehint checks:

<code>python -m mypy simple_type_hint.py</code>

### In case of an imbalance:
- If balance factor is greater than 1, then the current node is unbalanced and we are either in Left Left case or left Right case. To check whether it is left left case or not, compare the newly inserted key with the key in left subtree root. 
- If balance factor is less than -1, then the current node is unbalanced and we are either in Right Right case or Right-Left case. To check whether it is Right Right case or not, compare the newly inserted key with the key in right subtree root. 