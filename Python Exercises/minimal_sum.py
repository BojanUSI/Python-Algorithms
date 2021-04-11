def minimal_sum(A, x):
    total_sum = 0
    for a in A:
        if a >= x:
            return True
        if a > 0:
            total_sum += a
            if total_sum >= x:
                return True
    return False
