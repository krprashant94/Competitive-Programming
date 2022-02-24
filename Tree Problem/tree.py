#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tree:
    """Binary search tree"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)
        else:
            pass    
    
    def __repr__(self):
        """
        https://stackoverflow.com/a/54074933/3404480

        Returns
        -------
        None.

        """
        lines, *_ = self._display_aux()
        return '\n'.join(lines)

    def _display_aux(self):
       """Returns list of strings, width, height, and horizontal coordinate of the root."""
       # No child.
       if self.right is None and self.left is None:
           line = '%s' % self.value
           width = len(line)
           height = 1
           middle = width // 2
           return [line], width, height, middle

       # Only left child.
       if self.right is None:
           lines, n, p, x = self.left._display_aux()
           s = '%s' % self.value
           u = len(s)
           first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
           second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
           shifted_lines = [line + u * ' ' for line in lines]
           return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

       # Only right child.
       if self.left is None:
           lines, n, p, x = self.right._display_aux()
           s = '%s' % self.value
           u = len(s)
           first_line = s + x * '_' + (n - x) * ' '
           second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
           shifted_lines = [u * ' ' + line for line in lines]
           return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

       # Two children.
       left, n, p, x = self.left._display_aux()
       right, m, q, y = self.right._display_aux()
       s = '%s' % self.value
       u = len(s)
       first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
       second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
       if p < q:
           left += [n * ' '] * (q - p)
       elif q < p:
           right += [m * ' '] * (p - q)
       zipped_lines = zip(left, right)
       lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
       return lines, n + m + u, max(p, q) + 2, n + u // 2



if __name__ == "__main__":
    t = Tree(60)
    t.insert(30)
    t.insert(56)
    t.insert(4)
    t.insert(80)
    t.insert(10)
    t.insert(75)
    t.insert(35)
    t.insert(95)
    t.insert(69)
    t.insert(2)
    t.insert(69)
    t.insert(57)
    t.print()