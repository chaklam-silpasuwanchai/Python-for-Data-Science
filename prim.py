from heapdict import heapdict

G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

N = 5

Q = heapdict()
Q[0] = 0
Q[1] = 9999
Q[2] = 9999
Q[3] = 9999
Q[4] = 9999

parents    = [None] * 5
parents[0] = -1 #vertex 0 has no parent

def is_inside_queue(Q, v):
    if v in list(Q.keys()):
        return True
    return False
    
def adj(G, u):
    neighbors = []
    for v in range(N):
        if(G[u][v]):
            neighbors.append(v)
    return neighbors

while(Q):
    u = Q.popitem()[0]
    for v in adj(G, u):
        if (is_inside_queue(Q, v) and G[u][v] < Q[v]):
            Q[v] = G[u][v]
            parents[v] = u

print(parents)                

            


