def maximum(A):
    maxi = A[0]
    for a in A:
        if a > maxi:
            maxi = a
    return maxi

def maximal_increasing_subsequence(A):
    sequence = []
    counter = 1
    for i in range(len(A)-1):
        if A[i+1] > A[i]:
            counter += 1
            continue
        if counter >= 2:
            sequence.append(counter)
            counter = 1
    
    return(maximum(sequence))
