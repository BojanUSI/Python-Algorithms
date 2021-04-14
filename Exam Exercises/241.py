def two_primes(n):
    S = []
    for i in range(2, n):
        if prime_number(i) == True:
            S.append(i)
    
    for i in range(len(S) - 1):
        for j in range(i+1, len(S)):
            if S[i] + S[j] == n:
                return True
    
    return False




def prime_number(num):
    # Program to check if a number is prime or not

    # To take input from the user
    #num = int(input("Enter a number: "))

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True