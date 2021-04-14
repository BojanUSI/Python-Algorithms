def intervals_union(X):
    num = []
    for i in range(len(X)):
        x = X[i][0]
        while x <= X[i][1]:
            num.append(x)
            x += 1
    
    num.sort()
    
    S = []

    minl = num[0]
    for i in range(len(num)-1):
        if num[i] == num[i+1] or num[i]+1 == num[i+1]:
            continue
        else:
            maxl = num[i]
            t = (minl, maxl)
            S.append(t)
            minl = num[i+1]

    t = (minl, num[len(num)-1])
    S.append(t)
    return S



