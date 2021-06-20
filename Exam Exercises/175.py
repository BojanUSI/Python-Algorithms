class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

T = []

def bst_least_difference(t):
    global T
    D  = []
    X = print_in_order(t)
    for i in range(len(T)-1):
        D.append(T[i+1]-T[i])
    
    return min(D)

def print_in_order(t):
    global T
    if t != None:
        print_in_order(t.left)
        T.append(t.key)
        print_in_order(t.right)



t = Node(50)
t.left = Node(25)
t.left.left = Node(15)
t.left.right = Node (35)
t.right = Node(128)
t.right.left = Node(120)
t.right.left.left = Node(115)
t.right.right = Node(133)