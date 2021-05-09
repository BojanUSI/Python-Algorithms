def count_horizontal(A):
    c = 0
    for i in range(len(A)-1):
        if i % 2 == 1:
            for j in range(i+1, len(A)):
                if j % 2 == 1:
                    if A[i] == A[j]:
                        c += 1
    
    return c

def count_vertical(A):
    c = 0
    for i in range(len(A)-1):
        if i % 2 == 0:
            for j in range(i+1, len(A)):
                if j % 2 == 0:
                    if A[i] == A[j]:
                        c += 1
    
    return c

    # Complexity O(n^2)
    # i goes to n
    # j goes to i+1 to n on every iteration

def make_segments(A):
    S = []
    for i in range(len(A)):
        if i % 2 == 0:
            t = (A[i], A[i+1])
            S.append(t)
    
    return S


def intersection(A):
    X = make_segments(A)
    for i in range(len(X)-1):
        for j in range(i+1, len(X)):
            ...