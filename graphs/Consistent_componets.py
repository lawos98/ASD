"""
/=========================================================================================\
|Sprawdzanie ile jest spójnych składowych                                                 |
|                                                                                         |
|Policzyc liczbe spójnych składowych w grafie (implementacja przeciwna do tej z           |
|poprzedniego zadania)                                                                    |
|                                                                                         |
|Algorytm opiera się na typowym problemie grafowym a mianowicie przechodzimy po grafie    |
|DFS dochądzać do wszystkich wierzchołków które są na ścieżce z pumktem początkowym       |
|i owa operacja stanowi jedną spójną składową.Powtarzamy aż do momentu gdy wszystkie      |
|wierzchołki były odwiedzone                                                              |
|                                                                                         |
|Złożoność czasowa :O(V+E)             Złożoność Pamięciowa O(1)                          |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -liczba spójnych składowych                         |
|                                                                                         |
\=========================================================================================/
"""

def consistent_components(Array):
    n=len(Array)
    Visited=[-1 for _ in range(n)]
    def DFS(u):
        nonlocal n,Visited,Array
        for v in Array[u]:
            if Visited[v]==-1:
                n-=1
                Visited[v]=1
                DFS(v)
    index=0
    counter=0
    while n!=0:
        if Visited[index]==-1:
            DFS(index)
            counter+=1
        index+=1
    return counter


#end
