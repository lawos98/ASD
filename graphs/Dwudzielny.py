"""
/=========================================================================================\
|Sprawdzanie czy graf jest dwudzielny                                                     |
|                                                                                         |
|Sprawdzanie czy graf jest dwudzielny (czyli zauwazyc, ze to 2-kolorowanie                |
| i uzyc DFS lub BFS).                                                                    |
|                                                                                         |
|Algorytm opiera się na typowym problemie grafowym a mianowicie przechodzimy po grafie    |
|DFS przypisując dwie różen wartości logiczne sąsiedmin wierzchołkom, jeżeli dwa          |
|wierzchołki o tych samych wartościahc logicznych oznacza to że graf dwudzielny nie       |
|może powstać oraz w przypadku kiedy nie dotrzemy do wszystkich wierzchołków(niespójność) |
|w przeciwnym wypadku oznacza że możemy utworzyć graf dwudzielny                          |
|                                                                                         |
|Złożoność czasowa :O(V+E)             Złożoność Pamięciowa O(1)                          |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -istnienie grafu dwudzielnego                       |
|                                                                                         |
\=========================================================================================/
"""
def dwudzielny(G):
    n = len(G)
    visited = [None] * n

    def dfs(i, color):
        for v in G[i]:
            if visited[v] is None:
                visited[v] = color
                if not dfs(v, not color):
                    return False
            elif visited[v] != color:
                return False

        return True

    return dfs(0, False)


#end
