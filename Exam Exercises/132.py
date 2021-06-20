class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

def bst_print_longest_path(t):

    if t == None:
        return []
    
    r = bst_print_longest_path(t.right)
    l = bst_print_longest_path(t.left)

    if len(l) > len(r):
        l.append(t.key)
    else:
        r.append(t.key)
    
    if len(l) > len(r):
        return l
    
    else:
        return r

t = Node(10)
t.left = Node(8)
t.left.left = Node(5)
t.left.left.left = Node(2)
t.left.left.right = Node(7)
t.left.right = Node(9)
t.right = Node(20)
t.right.right = Node(30)
t.right.right.right = Node(31)
t.right.right.left = Node(25)
t.right.right.left.left = Node (24)
t.right.right.left.left.left = Node(23)
t.right.right.left.left.left.left = Node(22)