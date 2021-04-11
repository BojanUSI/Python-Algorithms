def equal_sum_seq(A):

    X = []
    
    for i in range(len(A)):
        sum = 0
        u = A[i]
        for j in range(i, len(A)):
            sum += A[j]
            for x in X:
                if x == sum:
                    return True
            X.append(sum)
    return False