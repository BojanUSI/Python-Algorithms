Q = [None]*100
# Fixed size array to store elements in the queue

Front = 0
# Points to the element that is in front of the queue

Back = 0
# Points to the first element past the last in the queue,
# which is where next element is enqueued


# Next position
def next(p):
    global Q
    p += 1
    if p == len(Q):
        p = 0
    return p


def is_empty():
    global Front, Back
    return Front == Back


def is_full():
    global Front, Back
    return next(Back) == Front


def enqueue(x):
    global Q, Front, Back
    if is_full():
        print("Queue is full.")
    else:
        Q[Back] = x
        Back = next(Back)


def dequeue():
    global Q, Front, Back
    if is_empty():
        print("Quene is empty.")
    else:
        x = Q[Front]
        Front = next(Front)
        return x