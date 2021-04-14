def high_power_run(A,h,t):
    j = 0
    h_cur = 0 # value of sliding window
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            h_cur += A[i] - A[i-1]
        if i > j + t:
            j += 1
            if A[j] > A[j-1]:
                h_cur -= A[j] - A[j-1]
        if h_cur >= h:
            print(i, j)
            return True
    return False