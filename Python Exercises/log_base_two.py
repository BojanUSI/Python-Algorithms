def log_base_two(n):
    k = 0
    while 2**k <= n:
        k += 1
    
    return k-1