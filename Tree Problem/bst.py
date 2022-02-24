#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tree import Tree
import random

root = Tree(250)
for i in range(30):
    root.insert(random.randint(1, 500))

def bst(root, el):
    if root.value == el:
        return "Found"
    elif root.value > el and root.left is not None:
        return bst(root.left, el)
    elif root.value < el and root.right is not None:
        return bst(root.right, el)
    else:
        return "Not Found"

print(root)
el = 230
print(bst(root, el))
