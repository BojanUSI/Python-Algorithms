def maximal_non_adjacent_sequence_weight(A):

    # DP(A,i) = max value in A[0, ..., i]
    # DP(A, i+1) = max {DP(A, i-1) + A[i+1], DP(A, i)}

    if len(A) < 1:
        return None
    
    if len(A) < 2:
        A[0]
    
    dp = A[1]
    dp_prev = A[0]
    max_value = max(dp, dp_prev)

    for i in range(2, len(A)):
        dp_prev, dp = dp, max(dp, dp_prev + A[i])
        max_value = max(max_value, dp)
    
    return max_value