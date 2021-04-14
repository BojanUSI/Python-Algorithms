def sum_of_three(A, s):
    B = merge_sort(A, 0, len(A))
    for i in range(len(A)):
        j = 0
        k = len(A) - 1
        while j < k:
            if j == i:
                j += 1
            elif k == i:
                k -= 1
            elif B[i] + B[j] + B[k] == s:
                return True
            elif B[i] + B[j] + B[k] > s:
                k -= 1
            else:
                j += 1
    return False

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

def merge_sort(A, begin, end):
    
    # Complexity: Θ(nlog n)

    # A - array
    # begin - the first index of the range of A we want
    # to be merge-sorted
    # end - the one-past-last index of the range of A
    # we want to be merge-sorted

    # Example: A[1, 2, 3, 4, 5, 6, 7, 8]
    #            ^ begin=0   ^ m=4       ^ end=8
    
    # Base case
    if end - begin == 1:
        return [A[begin]]
    elif end - begin == 0:
        return []

    m = (begin + end) // 2
    L = merge_sort(A, begin, m) # excludes position m
    R = merge_sort(A, m, end)   # excludes position end
    return merge(L, R)



def merge(A, B):
    # A, B sorted arrays
    # Return array X := combination of A and B
    # X needs to be sorted
    X = []

    i, j = 0, 0
    # i - index A
    # j - index B

    while i < len(A) or j < len(B):
        # find the minimum between A[i] (if it exists)
        # and B[j] (if it exists)

        # Two cases:
        # 1) We append A[i], then i = i + 1
        # 2) We append B[j], then j = j + 1

        # A[i] has to be there and either there is
        # no element in B, or there is, but A[i] is smaller.
        if i < len(A) and (j >= len(B) or A[i] <= B[j]):
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1

    return X

