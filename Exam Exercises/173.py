# Exercise 173:

def algo_x(A):

    # Finds the maximal difference between any two elements
    # Complexity: O(n^2)

    i = 1
    j = 0
    x = float('-inf')
    while i < len(A):
        if abs(A[i] - A[j]) > x:
            x = abs(A[i] - A[j])
        
        j += 1
        if j == i:
            i += 1
            j = 0
    
    return x


def better_algo_x(A):

    # In linear time finds the max and min in a sequence
    # and returns max - min

    # Complexity: Θ(n)

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