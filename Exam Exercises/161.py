# Exercise 161

from binary_search import *


# Question 1:
def find_elements_at_distance(A, k):

    # Complexity: O(n logn)
    # Binary search runs in logn and the outer
    # loop runs n times

    for i in range(len(A)):
        
        if binary_search(A, k + A[i]):
            return True
    
    return False



# Question 2:
def find_elements_at_distance_2(A, k):

    # Complexity: Θ(n)
    # In each iteration of the loop we either increase 
    # j or i by one (or we return). Also, the loop is 
    # such that j ≥ i, so in at most Θ(n) iterations
    # we push j beyond A.length. Thus the complexity 
    # is Θ(n).

    i = 0
    j = 1

    while j <= len(A):
    
        if A[j] - A[i] < k:
            j += 1
        elif A[j] - A[i] > k:
            i += 1
        else:
            return True
    
    return False
