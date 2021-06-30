from math import inf
from queue import PriorityQueue


def Dikstry(Array,s):
    n=len(Array)
    d=[inf]*n
    parent=[-1]*n
    d[s]=0
    Q=PriorityQueue()
    Q.put([d[s],s])
    while not Q.empty():
        u=Q.get()
        u=u[1]
        for v,w in Array[u]:
            if d[u]+w<d[v]:
                d[v]=d[u]+w
                Q.put([d[v],v])
                parent[v]=u
    print(parent)


from math import inf


def dijkstra(G, A, B):
    n = len(G)

    d = [inf] * n
    d[A] = 0

    visited = [False] * n

    for _ in range(n):
        u = min(range(n), key=lambda u: inf if visited[u] else d[u])
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]

    return d
