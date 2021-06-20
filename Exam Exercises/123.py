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

def connected():
    n = len(V)

    # BFS(G, 0)

    # Queue
    Q = [0]
    # Index in queue (head of queue)
    head = 0

    Visited = [False]*n
    Visited[0] = True
    count = 1
    while head < len(Q):
        v = Q[head]
        head += 1
        for u in Adj[v]:
            if  not Visited[u]:
                Visited[u] = True
                Q.append(u)
                count += 1

    if count == n:
        return True
    else:
        return False

def eulerian():
    if not connected():
        return False
    else:
        Deg = []
        for i in range(len(V)):
            Deg.append(len(Adj[i]))
        
        check = False
        for d in range(len(Deg)-1):
            if Deg[d] == Deg[d+1]:
                check = True
            else:
                check = False
                break
        
        return check
                

