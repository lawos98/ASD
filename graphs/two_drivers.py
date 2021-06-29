"""
/=========================================================================================\
|Przewodnik turystyczny                                                                   |
|                                                                                         |
|Dana jest mapa kraju w postaci grafu G = (V,E), gdzie wierzchołki to                     |
|miasta a krawedzie to drogi łaczace miasta. Dla kazdej drogi znana jest jej długosc      |
|(wyrazona w kilometrach jako liczba naturalna). Alicja i Bob prowadza (na zmiane)        |
|autobus z miasta x > V do miasta y > V , zamieniajac sie za kierownica w kazdym          |
|kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy. Prosze      |
|zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzic          |
|pierwsza), zeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien byc jak    |
|najszybszy (ale przede wszystkim poprawny).                                              |
|                                                                                         |
|Algorytym opiera się na algorytmie Dikstry w którym relaksacja oblicza odległość co      |
|drugiej krawędzi.Co za tym idzie algorytm najpierw wylicza w przypadku gdy nasz kierowca |
|zaczyna trase jak i w sytuacji kiedy jest drugi                                          |
|                                                                                         |
|Złożoność czasowa :O(E*log(V))      Złożoność Pamięciowa O(E*log(V)) )                   |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Listwa sąsiedztwa                  -Osoba starująca                                    |
| -punkt startowy                     -Trasa przejazdu                                    |
| -punkt końcowy                                                                          |
|                                                                                         |
\=========================================================================================/
"""


from queue import PriorityQueue

def relaxModified(u,v,w,d,parent,edges,evenOrOdd):
    if edges[u] % 2 == (evenOrOdd+1)%2 and d[v] > d[u]: #jeśli evenOrOdd == 0 to ten ktoś idzie po nieparzystych
        d[v] = d[u]
        parent[v] = u
        edges[v] = edges[u] + 1

    if edges[u] % 2 == (evenOrOdd)%2 and d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u
        edges[v] = edges[u] + 1

def dijkstraAliceBob(G,evenOrOdd,s,e):
    #G to lista adjacencji składująca tuple (dokąd,cena)
    q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    edges = [None for _ in range(n)]
    edges[s] = 0
    d[s] = 0
    q.put((0,s))
    while not q.empty():
        u = q.get()
        if not visited[u[1]]:
            visited[u[1]] = True
            for i in G[u[1]]:
                relaxModified(u[1],i[0],i[1],d,parent,edges,evenOrOdd)
                q.put((d[i[0]],i[0]))
    return d[e],parent

def solve(G,s,e):
    resOdd, pOdd = dijkstraAliceBob(G,0,s,e)
    resEven, pEven = dijkstraAliceBob(G,1,s,e)
    solution = []
    if resOdd > resEven:
        whoFirst = "B"
        better = pEven
    else:
        whoFirst = "A"
        better = pOdd
    i = e
    while better[i] != -1:
        solution.append(i)
        i = better[i]
    return whoFirst,solution
