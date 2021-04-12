# Exercise 192

def is_good(x):
    if x % 2 == 0:
        return True
    else:
        return False


def good_are_adjacent(A):
    c = 0
    for i in range(len(A)-1):
        if (is_good(A[i]) and is_good(A[i+1])) or \
        (not is_good(A[i]) and not is_good(A[i+1])):
            i += 1
        else:
            c += 1
    
    if c <= 1:
        return True
    else:
        return False
    

def make_good_adjacent(A):
    q = 0
    for i in range(len(A)):
        if is_good(A[i]):
            A[i], A[q] = A[q], A[i]
            q += 1


