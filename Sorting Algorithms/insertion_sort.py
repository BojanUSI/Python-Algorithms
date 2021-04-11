# Insertion sort:
# Average Case: θ(n^2)
# Best Case: θ(n) - array already sorted
# Worst Case: θ(n^2) - array in reverse order

def insertion_sort_increasing(A):
    # outer for-loop runs len(A)-1 times
    for i in range(1, len(A)):              
        j = i
        # best case: while-loop is never executed
        # worst case: while-loop executed j-1 times
        # for every for-loop execution
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

def insertion_sort_decreasing(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] > A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1 