"""
/=========================================================================================\
|Najkrótsza ścieżka za pomocą BFS                                                         |
|                                                                                         |
|Prosze zaimplementowac algorytm BFS tak, zeby znajdował                                  |
|najkrótsze sciezki w grafie i nastepnie, zeby dało sie wypisac najkrotsza sciezke        |
|z zadanego punktu startowego do wskazanego wierzchołka.                                  |
|                                                                                         |
|Algorytm opiera się na BFS a mianowicie przechodząc do następnej "fali" jeżeli           |
|wierzchołek nie był odiwedzony dodajnemy jeden do odległości                             |
|                                                                                         |
|Złożoność czasowa :O(V+E)             Złożoność Pamięciowa O(V+E)                        |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Najkrótsza ścieżka z s to k                        |
| -Wierzchołek startowy                                                                   |
| -Wierzchołek końcowy                                                                    |
|                                                                                         |
\=========================================================================================/
"""

from queue import Queue

def BFS( G, s, k ):
    queue = Queue()
    visited = [False]*len(G)
    parent = [None]*len(G)
    distance = [None]*len(G)
    queue.put(s)
    visited[s] = True
    distance[s] = 0

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u]+1
                parent[v] = u
                queue.put(v)

    path = [k]

    while k != s:
        path=[parent[k]]+path
        k = parent[k]
    return path


#end
