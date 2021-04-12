# Exercise 179
# Complexity O(logN)

def unimodal_find_maximum(A):
    begin = 0
    end = len(A)

    while(begin < end):
        
        middle = (begin + end) // 2
        if end - begin == 2:
            return A[middle]
        if A[middle] > A[middle + 1]:
            end = middle + 1
        elif A[middle] < A[middle + 1]:
            begin = middle
    
    return A[middle]