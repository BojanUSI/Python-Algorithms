def peak_order(A):

    quick_sort_p(A, 0, len(A) // 2)
    quick_sort_n(A, len(A)//2, len(A))
    return A
    
def partition_p(A, begin, end):

    # Complexity: Θ(n)

    assert end - begin > 1

    # pick a pivot element: deterministically A[end-1]
    pivot = A[end - 1]
    q = begin

    for i in range(begin, end-1):
        if A[i] < pivot:
            A[i], A[q] = A[q], A[i]
            q += 1
        
    A[end-1], A[q] = A[q], A[end-1]
    return q

def partition_n(A, begin, end):

    # Complexity: Θ(n)

    assert end - begin > 1

    # pick a pivot element: deterministically A[end-1]
    pivot = A[end - 1]
    q = begin

    for i in range(begin, end-1):
        if A[i] > pivot:
            A[i], A[q] = A[q], A[i]
            q += 1
        
    A[end-1], A[q] = A[q], A[end-1]
    return q

def quick_sort_p(A, begin, end):

    # Worst case: q = begin or q = end - Θ(n^2)
    # Best case: q = [n/2] - Θ(n logn)

    if end - begin >= 2:
        q = partition_p(A, begin, end)
        quick_sort_p(A, begin, q)
        quick_sort_p(A, q+1, end)

def quick_sort_n(A, begin, end):

    # Worst case: q = begin or q = end - Θ(n^2)
    # Best case: q = [n/2] - Θ(n logn)

    if end - begin >= 2:
        q = partition_n(A, begin, end)
        quick_sort_n(A, begin, q)
        quick_sort_n(A, q+1, end)