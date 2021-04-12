def linear_search(A, v):
    # Complexity: O(n)
    for a in A:
        if a == v:
            return True
            
    return False