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

n = len(V)

src = 0

# BFS(G, src)

# Queue
Q = [src]
# Index in queue (head of queue)
head = 0

Visited = [False]*n
Visited[0] = True

# Distances from the source node src
D = [None]*n
D[src] = 0

# Previous nodes
P = [None]*n
P[src] = src

while head < len(Q):
    v = Q[head]
    head += 1
    for u in Adj[v]:
        if  not Visited[u]:
            P[u] = v
            D[u] = D[v] + 1
            Visited[u] = True
            Q.append(u)


for i in range(n):
    print('Node ', V[i], 'is at distance', D[i], 'from Node', V[src])