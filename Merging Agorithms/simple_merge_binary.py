# A and B are sorted arrays
def simple_merge_binary(A, B):
    X = []
    for a in A:
        if not binary_search(X, a):
            X.append(a)
    for b in B:
        if not binary_search(X, b):
            X.append(b)
    
    return X

def binary_search(A, key):
    begin = 0
    end = len(A)
    while begin < end:

        middle = (begin + end) // 2

        if A[middle] == key:
            return True
        elif A[middle] < key:
            begin = middle + 1
        else:
            end = middle
    
    return False
    