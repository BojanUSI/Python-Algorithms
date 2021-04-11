def find(T, val):
    # Complexity: O(n)
    for t in T:
        if t == val:
            return True
    
    return False

def simple_merge(A, B):
    # Complexity O(n^2)
    X = []
    for a in A:
        if not find(X, a):
            X.append(a)
    for b in B:
        if not find(X, b):
            X.append(b)
    return X