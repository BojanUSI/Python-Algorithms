def occurences(A):

    A.sort()
    counter = 1

    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            counter += 1
        else:
            print(A[i], counter)
            counter = 1

    print(A[len(A)-1], counter)
    
