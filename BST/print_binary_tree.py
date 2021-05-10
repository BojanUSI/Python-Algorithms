#!/usr/bin/python3

import sys

class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

class Canvas:
    def __init__(self,width):
        self.line_width = width
        self.canvas = []

    def put_char(self,x,y,c):
        if x < self.line_width:
            pos = y*self.line_width + x
            l = len(self.canvas)
            if pos < l:
                self.canvas[pos] = c
            else:
                self.canvas[l:] = [' ']*(pos - l)
                self.canvas.append(c)

    def print_out(self):
        i = 0
        sp = 0
        for c in self.canvas:
            if c != ' ':
                sys.stdout.write(' '*sp)
                sys.stdout.write(c)
                sp = 0
            else:
                sp += 1
            i = i + 1
            if i % self.line_width == 0:
                sys.stdout.write('\n')
                sp = 0
        if i % self.line_width != 0:
            sys.stdout.write('\n')

def print_binary_tree_r(t,x,y,canvas):
    max_y = y
    if t.left != None:
        x, max_y, lx, rx = print_binary_tree_r(t.left,x,y+2,canvas)
        x = x + 1
        for i in range(rx,x):
            canvas.put_char(i, y+1, '/')

    middle_l = x
    for c in str(t.key):
        canvas.put_char(x, y, c)
        x = x + 1
    middle_r = x

    if t.right != None:
        canvas.put_char(x, y+1, '\\')
        x = x + 1
        x0, max_y2, lx, rx = print_binary_tree_r(t.right,x,y+2,canvas)
        if max_y2 > max_y:
            max_y = max_y2
        for i in range(x,lx):
            canvas.put_char(i, y+1, '\\')
        x = x0

    return (x,max_y,middle_l,middle_r)

def print_tree(t):
    print_tree_w(t,20000)

def print_tree_w(t,width):
    canvas = Canvas(width)
    print_binary_tree_r(t,0,0,canvas)
    canvas.print_out()

t = Node(12)
t.left = Node(5)
t.left.left = Node(2)
t.left.left.right = Node(4)
t.left.right = Node (9)
t.right = Node(18)
t.right.left = Node(15)
t.right.left.left = Node(13)
t.right.right = Node(19)
t.right.left.right = Node(17)


# Print BST values in order:
def print_in_order(t):
    if t != None:
        print_in_order(t.left)
        print(t.key)
        print_in_order(t.right)


# Print size of BST:
def bst_size(t):
    if t == None:
        return 0
    else:
        return bst_size(t.right) + 1 + bst_size(t.left)


# Print height of BST:
def bst_height(t):
    if t == None:
        return 0
    else:
        return 1 + max(bst_height(t.left), bst_height(t.right))


# Print min of BST:
def bst_min(t):
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t.key

def bst_min_node(t):
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t

# Print max of BST:
def bst_max(t):
    if t == None:
        return None
    while t.right != None:
        t = t.right
    return t.key


# Print next and previous of key:
def bst_next(t):
    if t.right != None:
        return bst_min_node(t.right)
    p = t.parent
    while p != None and p.left != t:
        t = p
        p = p.parent
    return p

def bst_prev(v):
    pass

# Search for a key in BST:
def bst_search(t, k):
    while t != None and t.key != k:
        if k > t.key:
            t = t.right
        else:  
            t = t.left
    return t != None


# Insert a node in BST:
# Insert key k in BST at t
# t may be null
# keys may be repeated
# return the root of the (potentially new) tree
def bst_insert(t, k):
    if t == None:
        return Node(k)
    
    r = t

    while True:
        assert t != None
        if k <= t.key:
            if t.left != None:
                t = t.left
            else:
                t.left = Node(k)
                return r
        else:
            if t.right != None:
                t = t.right
            else:
                t.right = Node(k)
                return r

# Rotate BST:
def bst_right_rotate(t):
      r = t.left
      t.left = r.right
      r.right = t
      return r

def bst_left_rotate(t):
      r = t.right
      t.right = r.left
      r.left = t
      return r