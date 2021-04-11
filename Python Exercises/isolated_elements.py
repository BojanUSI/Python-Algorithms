def isolated_elements(A):
    if len(A) > 0:
        if A[0] != A[1]:
            print (A[0])
        for i in range(1, len(A)-1):
            if A[i] != A[i-1] and A[i] != A[i+1]:
                print(A[i])
        if A[len(A)-1] != A[len(A)-2]:
            print(A[len(A)-1])