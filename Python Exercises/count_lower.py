def count_lower(A, x):
    counter = 0
    for a in A:
        if a < x:
            counter += 1
    
    return counter