import math

def maximal_distance(X, Y):
    x1 = X[0]
    x2 = X[1]
    y1 = Y[0]
    y2 = Y[1]
    maxd = dist(x1,x2,y1,y2)
    for i in range(0, len(X)-1):
        for j in range(i+1, len(X)):
            d = dist(X[i], X[j], Y[i], Y[j])
            if d > maxd:
                maxd = d
                x1 = X[i]
                x2 = X[j]
                y1 = Y[i]
                y2 = Y[j]
    
    print("(",x1,",",y1,")")
    print("(",x2,",",y2,")")
        




def dist(x1, x2, y1, y2):
    return math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))