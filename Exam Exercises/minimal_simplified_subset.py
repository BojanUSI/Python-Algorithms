from linear_search import *

def minimal_simplified_subset(A):
    X = []
    Y = []
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            sum = 0
            sum = A[i] + A[j]
            if linear_search(A, sum):
                X.append(sum)
    
    for a in A:
        if not linear_search(X, a):
            Y.append(a)


    return Y
            




                

