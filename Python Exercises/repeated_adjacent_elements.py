def repeated_adjacent_elements(A):
    check = False
    for i in range(len(A)-1):
        if A[i] == A[i+1] and check == False:
            print(A[i])
            check = True
        elif A[i] != A[i+1]:
            check = False