class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def minimal_covering_square(P):
    x_p = P[0].x
    x_n = P[0].x

    y_p = P[0].y
    y_n = P[0].y

    for i in range(len(P)):
        if P[i].x > x_p:
            x_p = P[i].x
        elif P[i].x < x_n:
            x_n = P[i].x
    
    for i in range(len(P)):
        if P[i].y > y_p:
            y_p = P[i].y
        elif P[i].y < y_n:
            y_n = P[i].y
    

    if abs(x_p) + abs(x_n) > abs(y_p) + abs(y_n):
        return (abs(x_p) + abs(x_n))**2
    else:
        return (abs(y_p) + abs(y_n))**2