def algo_x(A, B):
    if algo_y(A, B) and algo_y(B, A):
        return True
    else:
        return False

def algo_y(A, B):                                   # Cost:
    X = [0]*len(A)                                  # c(1)
    for i in range(len(B)):                         # c(len(B))
        j = 0                                       # c(len(B))
        f = 0                                       # c(len(B))
        while j < len(A) and f == 0:                
            if X[j] == 0 and A[j] == -B[i]:
                X[j] = 1
                f = 1
            else:
                j += 1
        if f == 0:
            return False
    return True


def partition(A, begin, end):

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

def quick_sort(A, begin, end):

    # Worst case: q = begin or q = end - Θ(n^2)
    # Best case: q = [n/2] - Θ(n logn)

    if end - begin >= 2:
        q = partition(A, begin, end)
        quick_sort(A, begin, q)
        quick_sort(A, q+1, end)


def better_algo_x(A, B):

    if len(A) == len(B):
    
        A.sort(reverse =  True)
        B.sort()

        for i in range(len(A)):
            if A[i] != -B[i]:
                return False

        return True
    
    return False    
