def count_C(A):
    digs = [1] * 10
    for a in A:
        digs[a % 10] += 1
    c = 1
    for d in digs:
        c *= d
    
    return c-1
    
    
    

