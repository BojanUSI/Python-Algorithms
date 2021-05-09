class list_element:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    
L = None


def is_empty():
    global L
    return L == None


def insert_front(x):
    global L
    L = list_element(x, L)


def insert_after(x, v):
    x.next = list_element(v, x.next)


def insert_before(x, v):
    pass
    # Continue to double linked list

def delete_front():
    global L
    if L == None:
        print("List is empty.")
    else:
        L = L.next


def get_element_at(i):
    # Θ(n)
    global L
    l = L
    while l != None:
        if i == 0:
            return l.value
        i -= 1
        l = l.next
    print("Index out of bounds.")


def find(x):
    # Θ(n)
    global L
    l = L
    while l != None:
        if l.value == x:
            return l.value
        l = l.next
    print("Index out of bounds.")


def print_all():
    global L
    l = L
    while l != None:
        print(l.value)
        l = l.next


    