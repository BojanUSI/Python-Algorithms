def maximal_step_k_length(A,k):
    B = []
    for i in range(len(A)-1):
        B.append(A[i]-A[i+1])
    
    counter_n = 1
    counter_p = 1
    C = []
    for i in range(len(B) - 1):
        if (B[i] == B[i+1]) and B[i] == -k:
            counter_n += 1
            C.append(counter_n)
        elif (B[i] == B[i+1]) and B[i] == k:
            counter_p += 1
            C.append(counter_p)
        else:
            counter_n = 1
            counter_p = 1
    
    if len(C) >= 1:
        max = C[0]
        for c in C:
            if c > max:
                max = c
        
        return max + 1
    elif B[0] == k or B[0] == -k:
        return 2



        