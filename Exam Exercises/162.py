# Exercise 162

from prime_number import *

def partition_primes_composites(A):
    i = 0
    j = 0
    while i <= j and j < len(A):
        if prime_number(A[j]):
            A[j], A[i] = A[i], A[j]
            i += 1
            j = i
        else:
            j += 1



