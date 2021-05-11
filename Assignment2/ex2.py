class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

def bst_size(t):
    if t == None:
        return 0
    else:
        return bst_size(t.right) + 1 + bst_size(t.left)

Front = 0
# Points to the element that is in front of the queue

Back = 0
# Points to the first element past the last in the queue,
# which is where next element is enqueued

def next(Q, p):
    p += 1
    if p == len(Q):
        p = 0
    return p
def is_empty():
    global Front, Back
    return Front == Back
def is_full(Q):
    global Front, Back
    return next(Q, Back) == Front
def enqueue(Q, x):
    global Front, Back
    if is_full(Q):
        print("Queue is full.")
    else:
        Q[Back] = x
        Back = next(Q, Back)
def dequeue(Q):
    global Front, Back
    if is_empty():
        print("Queue is empty.")
    else:
        x = Q[Front]
        Front = next(Q, Front)
        return x

def print_bst_by_level(t):

    if t == None:
        return

    global Front, Back

    size = bst_size(t)
    if size == 1:
        return t.key
    else:
        Q =[None]*(2 * size)

    enqueue(Q, t)
    enqueue(Q, "separator")

    while True:
        current = dequeue(Q)
        if current != "separator":
            print(current.key, end = " ")
            if current.left != None:
                enqueue(Q, current.left)
            if current.right != None:
                enqueue(Q, current.right)
        else:
            print(" ")
            if is_empty():
                break
            else:
                enqueue(Q, "separator")
