def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return i // 2

def max_heapify(A, i):
    largest = i
    l = left(i)
    r = right(i)

    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A)//2, 1, -1):
        max_heapify(A,i)


# Complete

