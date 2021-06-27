"""
/=========================================================================================\
|Scieżka zawierająca malejące krawędzie                                                   |
|                                                                                         |
|Dany jest graf G = (V,E), gdzie kazda krawedz ma wage (wagi krawedzi sa parami rózne).   |
|Prosze zaproponowac algorytm, który dla danych wierzchołków x i y sprawdza,              |
|czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz              |
|mniejszych wagach.                                                                       |
|                                                                                         |
|Algorytm opiera się na BFS a mianowicie przechodząc do następnej "fali" jeżeli           |
|następna krawedź posiada wartość mniejszą od wierzchołka wejściowego oraz wierzchołek    |
|posiada najwięlszą wartość wejściową                                                     |
|                                                                                         |
|Złożoność czasowa :O(V+E)             Złożoność Pamięciowa O(V+E)                        |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Malejąca ścieżka z s to k                          |
| -Wierzchołek startowy                                                                   |
| -Wierzchołek końcowy                                                                    |
|                                                                                         |
\=========================================================================================/
"""

def BFS( G, s, k ):
    queue = Queue()
    parent = [None]*len(G)
    weight = [0]*len(G)
    queue.put(s)
    weight[s]=inf

    while not queue.empty():
        u = queue.get()
        for v,w in G[u]:
            if w<weight[u] and weight[v]<w:
                weight[v]=w
                parent[v]=u
                queue.put(v)
    path = [k]

    while k != s:
        path=[parent[k]]+path
        k = parent[k]
    return path


#end
