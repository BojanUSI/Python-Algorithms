def max(A):
    maxi = A[0]
    for a in A:
        if a > maxi:
            maxi = a
    return maxi

def maximal_step_k_length(A, k):
    
    counter = []
    array_is = "forward"
    counter_down = 1
    counter_up = 1
    for i in range(len(A)-1):

        if A[i] > A[i+1]:
            array_is = "backward"
            counter_up = 1
        else:
            array_is = "forward"
            counter_down = 1

        if array_is == "forward" and A[i] + k == A[i+1]:
            counter_up += 1
            counter.append(counter_up)
            continue
        elif array_is == "forward" and A[i] + k != A[i+1]:
            counter_up = 1
        
        if array_is == "backward" and A[i] - k == A[i+1]:
            counter_down += 1
            counter.append(counter_down)
            continue
        elif array_is == "backward" and A[i] - k != A[i+1]:
            counter_down = 1
    
    if len(counter) >= 2:
        return max(counter)
        

        

        

        