# The algorithm algo_x sorts the array based on the remainder of
# the current number when devided by 4. First are all numbers
# that have remainder 0, then 1, 2 and finally 3.

# The complexity in the worst case scenario is O(n^2).

def better_algo_x(A):

    X = [[], [], [], []]

    for i in range(len(A)):
        X[A[i] % 4].append(A[i])

    for i in range(4):
        X[i].sort()
    
    j = 0 

    for i in range(4):
        for x in X[i]:
            A[j] = x
            j += 1
    
    return A

# Couldn't come up with an O(n) solution, however, this has a better
# complexity of algo_x, or total complexity of O(n log n)
