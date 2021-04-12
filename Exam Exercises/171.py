# Exercise 171

from binary_search import *

def search_in_sorted_matrix(M, x):
    for i in range(len(M)):
        if binary_search(M[i], x):
            return True
    
    return False
