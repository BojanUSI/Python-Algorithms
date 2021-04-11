def merge(A, B):
    # Requirement:
    # A, B are sorted sequences

    # Complexity: Θ(n)
    # We cannot do better as we would skip elements otherwise

    # Return array X := combination of A and B
    # X needs to be sorted
    X = []

    i, j = 0, 0
    # i - index A
    # j - index B

    # One iteration can finish before the other one
    while i < len(A) or j < len(B):
        # find the minimum between A[i] (if it exists)
        # and B[j] (if it exists)

        # Two cases:
        # 1) We append A[i], then i = i + 1
        # 2) We append B[j], then j = j + 1

        # A[i] has to be there and either there is
        # no element in B, or there is, but A[i] is smaller.
        if i < len(A) and (j >= len(B) or A[i] <= B[j]):
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1

    return X
