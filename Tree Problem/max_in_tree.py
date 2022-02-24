#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tree import Tree
import random
root = Tree(250)
for i in range(30):
    root.insert(random.randint(1, 500))


a = 10
b = 120

print("Max element in range " + str(a) + " and " + str(b))
def getMax(node, a, b):
    while True:
        if a > b:
            a, b = b, a
        if node.value >= a and node.value <= b:
            if node.left == None and node.right == None:
                return node.value
            elif node.right is not None:
                if node.right.value <= b:
                    node = node.right
                else:
                    m = getMax(node.right, a, b)
                    if m is None or m < node.value:
                        return node.value
                    else:
                        return m
            elif node.left is not None:
                m = getMax(node.left, a, b)
                if m is None or m < node.value:
                    return node.value
                else:
                    return m
            else:
                return node.value
        elif node.value > b and node.left is not None:
            node = node.left
        elif node.value < a and node.right is not None:
            node = node.right
        else:
            return None

print(root)
print(getMax(root, a, b))

