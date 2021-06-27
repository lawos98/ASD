"""
/=========================================================================================\
|Wyłączanie sieci telefonicznej                                                           |
|                                                                                         |
|Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w             |
|Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich           |
|stacji nadawczych (które tworza spójny graf połaczen). Ze wzgledów technologicznych      |
|urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo zalezy na tym, by podczas  |
|całego procesu wszyscy abonenci znajdujacy sie w zasiegu działajacych stacji mogli sie   |
|ze soba łaczyc (czyli by graf pozostał spójny). Prosze zaproponowac algorytm             |
|podajacy kolejnosc wyłaczania stacji.                                                    |
|                                                                                         |
|Algorytm opiera się na typowym problemie grafowym a mianowicie przechodzimy po grafie    |
|DFS aż natrafimy na wierzchołek który nie prowadzi do żadnych nowych wierzchołków i      |
|owy wierzchołek "usuwamy" z naszej sieci                                                 |
|                                                                                         |
|Złożoność czasowa :O(V^2)             Złożoność Pamięciowa O(1)                          |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Macierz sąsiedztwa                 -Aktualna kolejność usuwanie sieci                  |
|                                                                                         |
\=========================================================================================/
"""
def take_off_network(G):
    def DFS(G, v, result, visited):
        visited[v] = True
        for u in range(len(G)):
            if G[v][u] == 1 and visited[u] == False:
                DFS(G, u, result, visited)
        result+=[v]

    result = []
    visited = [False] * len(G)
    DFS(G, 0, result, visited)
    return result


#end
