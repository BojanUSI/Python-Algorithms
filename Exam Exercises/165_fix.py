def algo_x(n):              
    c = 0
    a = n
    while a > 1:                
        b = 1
        while b <= a*a:
            c += 1
            b = 2*b
        a = a//2
    
    return c