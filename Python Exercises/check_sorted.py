def check_sorted(A):
    for i in range(len(A)-1):
        if A[i] <= A[i+1]:
            continue
        else:
            return False
    
    return True