def linear_search(A, v, i):

    # Parameters:
    # A - array 
    # v - value that we are looking for
    # i - index where v appears in A
    
    # Description:
    # Goes through entire array and checks whether parmeter
    # v matches with the element in array A at position x

    # Complexity:
    # O(n) - linear search
    # Best case:
    # The element we are looking for is found in the first iteration - O(1)
    # Worst case:
    # The element we are looking for is not found in A (and therefore is unique) - O(n)

    for x in range(len(A)):
        if i == x:
            continue
        elif A[x] == v:
            return True
            
    return False

def first_unique(A):

    # Parameters:
    # A - array

    # Description:
    # Goes from range 0 to len(A) and executes linear_search on every
    # element of the array at position i to check whether the same element
    # appears again in the array. If there are no other occurrences of that
    # element (the linear_search returns False) that means the element is unique.

    # Complexity:
    # Average case: O(n^2) - linear_search is performed n times and depending
    # on the size of A, the number of searches increases exponentially

    # Worst case: O(n^2) - there is no unique element in the array A.
    # linear_search is called n times and the for-loop inside is also
    # executed n times (where n = len(A)). The function linear_search always
    # returns True (the element is not unique) and first_unique doesn't return anything.

    # Example worst-case input: first_unique([1,2,3,4,5,1,2,3,4,5])
    # O(n^2)

    for i in range(len(A)):
        if linear_search(A, A[i], i) == False:
            return A[i]


        
