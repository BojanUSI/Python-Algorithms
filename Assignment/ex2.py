# Question 1:
# The algorithm performs all possible combinations of sums between the elements in A and puts the separate unique results in B.
# Repeated elements are excluded from B with the function algo_y which performs a linear search in B. If there is a single element
# in B such that it is strictly less than the input parameter x, algo_x returns True (and False otherwise).

# Question 2:

# Worst case complexity:
# Θ(2^n) - All combinations of sums are unique and every separate sum is appended to B. The algorithm algo_y always returns True as
# there will be no other equal sum already in the array. As i in the outer loop increases, the inner loop will execute 2^i new calculations,
# and append every new result separately in B.
# Example imput: algo_x([5, 10, 20], 0) - This would produce a total of 2^len(A) (= 8) new and unique combinations and store them in B.
# It will run the outer for-loop 3 times and depending on the i produce 2^i combinations in every inner for-loop.

# Best case complexity:
# Θ(n) - All combination of sums are identical to each other. In this case since B already has an element 0, that means that all other combinations
# would equal 0. This way algo_y would always return False.
# Example imput: algo_x([0, 0, 0], 0) - The outer and inner for-loops will be exectued len(A) and len(B) times correspondingly but all combinations
# will be equal to each other and therefore algo_y will run in constant time (exit on the first iteration).



def algo_x(A,x):
    B = [0]
    for i in range(len(A)):
        l = len(B)
        for j in range(0, l):
            s = B[j] + A[i]
            if algo_y(B, s):
                B.append(s)
    
    for i in range(len(B)):
        if x >= B[i]:
            return True

    return False

def algo_y(A,x):
    for i in range(len(A)):
        if x == A[i]:
            return False
    
    return True



def better_algo_x(A, x):
    s = 0
    for i in range(len(A)):
        if x >= 0:
            return True
        elif A[i] < 0:
            s += A[i]
            if x >= s:
                return True
    
    return False


# The algorithm goes through all elements in array A and depending on current i, then performs an addition between A[i]
# and all elements in B that are in a range of [0, 2^i] as the length of B exponentially increases. 
# If the newly computed element is already in the array B it is not appended to B. At the end B has a size of 2^(len(A)) minus the repeated elements.

# Worst case scenario:  When we input an array in A such that all elements when added produce a new (never repeated) result. Therefore B after computation,
# will have a size 2^len(A). For example A=[5, 100, 200, 400]. 

# Best case scenario: Absolute best scenario is when all elements in Array A = 0. The resulting B array will only consist of a single element: 0.
# Another best case scenario when the input doesn't consist of only 0 elements, is when all elements are equal to each other and are not 0.

