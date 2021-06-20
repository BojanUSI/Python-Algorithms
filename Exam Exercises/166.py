import sys

V = []
Adj = []
V_idx = {} 


# strip() - removes spaces in front or behind
# split() - splits words into differenet array elements

for line in sys.stdin:
    A = line.strip().split()
    for v in A:
        # v is a string, vertex name
        if not v in V_idx:
            V_idx[v] = len(V)
            V.append(v)
            Adj.append([])
    
    v_i = V_idx[A[0]]
    for i in range(1, len(A)):
        u_i = V_idx[A[i]]
        Adj[v_i].append(u_i)


Visited = [False]*len(V)
Previous = [None]*len(V)


def find_cycle():

    for i in range(len(V)):
        if not Visited[i]:
            Visited[i] = True
            if find_cycle_r(Visited, Previous, i):
                return True
    
    return False

def find_cycle_r(Visited, Previous, v):
    for w in Adj[v]:
        if Visited[w]:
            u = Previous[v]
            while u != None:
                if u == w:
                    return True
                u = Previous[u]
        else:
            Visited[w] = True
            Previous[w] = v
            if find_cycle_r(Visited, Previous, w):
                return True
    return False