def increasing_or_decreasing(A):

    check = 0
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            check = 0
        else:
            check = 1
            break
    if check == 0:
        return "flat"

    # Cost O(n), linearly goes through entire array

    T = []
    for i in range(len(A)-1):
        T.append(A[i] - A[i+1])

    # Cost O(n), linearly appends the difference between
    # two adjacent elements
    
    dec = 1
    D = []
    inc = 1
    I = []
    for i in range(len(T)-1):
        if T[i] <= 0 and T[i+1] <= 0:
            inc = 1
            dec += 1
            D.append(dec)
        elif T[i] >= 0 and T[i+1] >= 0:
            dec = 1
            inc += 1
            I.append(inc)
        else:
            inc = 1
            dec = 1
    
    # Cost O(n), linearly goes through all elements in T
    # and adapts D and I adequatly in O(n) time.
    
    
    if len(D) > 0:
        maxdec = D[0]
        for d in D:
            if d > maxdec:
                maxdec = d
    else:
        maxdec = 1
    
    if len(I) > 0:
        maxinc = I[0]
        for i in I:
            if i > maxinc:
                maxinc = i
    else:
        maxinc = 1
    
    # Cost O(n), finding the maximum values in D and I
    # takes linear time

    if maxinc > maxdec:
        return "decreasing"
    elif maxinc < maxdec:
        return "increasing"
    elif maxinc == maxdec:
        return "equal"

    # Cost O(1):

    # Total cost: 4*O(n) = O(n)


