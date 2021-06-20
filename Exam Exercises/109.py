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
        Adj[u_i].append(v_i)
        Adj[v_i].append(u_i)

def is_edge(u, v):
    for i in Adj[u]:
        if i == v:
            return True
    return False

def find_triangle():
    for i in range(len(V)):
        for v in Adj[i]:
            for j in range(len(V)):
                if is_edge(v, j) and is_edge(i, j):
                    return True
    return False
