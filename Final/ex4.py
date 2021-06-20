# Question 1:
# The idea would be to make 2 arrays of all sub sequences and
# check for the longest contiguous subsequence. However, this solution
# is non-polynomial - O(2 ^ (2*len(A))

def longest_mirror_seq(A, B):

    # len(A) == len(B)

    # Using dynamic programming and a DP matrix

    # DP[i][j] - longest contigious sequence of A[i:] and B[j:]
    # If for any index i and j A[i] == A[j] that means that
    # DP[i][j] = 1 + DP[i+1][j+1] (+1 as we have found a longer subsequence)
    # Therefore, the maximum element in the DP matrix is the length of
    # the longest contguous subsequence

    # Reversing B:
    # Complexity O(n)
    B = B[::-1]

    # Lengths of array A and B:
    x = len(A)
    matrix_x = x - 1

    # Creating an n x n matrix in python:
    # Complexity O(n^2) as well as space complexity of n^2
    DP = []

    for i in range(len(A)+1):
        DP.append([])
        for j in range(len(B)+1):
            DP[i].append(0)

    # Checking for the combinations in the matrix:
    # Complexity: O(n^2)
    for j in range(matrix_x, -1, -1):
        for i in range(matrix_x, -1, -1):
            if A[j] == B[i]:
                DP[i][j] = 1 + DP[i+1][j+1]
    

    # Find the maximum length in the DP matrix:
    # Set to 0 as we cannot have a negative length, so the least possible
    # length is 0
    # Complexity: O(n^2)
    max_length = 0

    for x in DP:
        for y in x:
            if y > max_length:
                max_length = y
    
    return max_length

    # Total complexity 4*O(n^2) = O(n^2)








    
