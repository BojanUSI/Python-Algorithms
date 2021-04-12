# Exercise 187

def most_congested_segment(A, l):

    D = []

    for a in A:
        counter = 1
        for b in A:
            if b > a and b <= a + l:
                counter += 1
        D.append(counter)
    
    max = D[0]
    max_p = 0
    for d in range(len(D)):
        if D[d] > max:
            max = D[d]
            max_p = d
    
    return str(A[max_p]) + " to " + str(A[max_p] + l)

