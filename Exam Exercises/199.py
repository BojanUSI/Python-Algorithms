# Exercise 199

def maximal_distance(A):
    if len(A) < 2:
        return 0
    max = A[0]
    min = A[0]
    for a in A:
        if a > max:
            max = a
        elif a < min:
            min = a
    
    return max - min