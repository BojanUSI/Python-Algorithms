def binary_search(A, key):
    # Complexity: O(log n)
    begin = 0
    end = len(A)
    while begin < end:

        middle = (begin + end) // 2

        if A[middle] == key:
            return True
        elif A[middle] < key:
            begin = middle + 1
        else:
            end = middle
    
    return False