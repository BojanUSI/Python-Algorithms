# The algorithm checks whether there are k elements in the array
# such that the result of those elements squared is also in the array
# The square of the first element is neglected.
# Total complexity of this algorithim is O(n^2)

def better_algo_y(A, k):
    X = []
    Y = []
    c = 0
    for i in range(1, len(A)):
        X.append(i*i)
    for a in A:
        Y.append(a)
    
    Y.sort()

    for x in X:
        if x in Y:
            c += 1
        if c >= k:
            return True
    
    return False

# Total complexity of better_algo_y is O(n log n) in best and worst case.
# We always sort Y and have complexity of  n log n.