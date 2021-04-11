def linear_search(A, v):
    # Complexity: O(n)
    for a in A:
        if a == v:
            return True
            
    return False

def minimal_simplified_subset(A):
    X = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            s = A[i] + A[j]
            if linear_search(A, s):
                X.append(s)

    for i in range(len(A)):
        for j in range(len(X)):
            if A[i] == A[j]:
                A.pop(i)

    return A

                

