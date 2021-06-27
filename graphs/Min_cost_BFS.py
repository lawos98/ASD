"""
/=========================================================================================\
|Scieżka zawierająca malejące krawędzie                                                   |
|                                                                                         |
|Dana jest mapa kraju w postaci grafu G = (V,E). Kierowca chce przejechac                 |
|z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawedzie)                |
|sa płatne. Kazda droga ma taka                                                           |
|                                                                                         |
|Algorytm opiera się na BFS a mianowicie przechodząc do następnego wierzchołka który ma   |
|minimalny koszt.                                                                         |
|                                                                                         |
|Złożoność czasowa :O(V+E)             Złożoność Pamięciowa O(V+E)                        |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Minimalna ścieżka z s to k                         |
| -Wierzchołek startowy                                                                   |
| -Wierzchołek końcowy                                                                    |
|                                                                                         |
\=========================================================================================/
"""
def BFS( G, s, k ):
	n=len(G)
	queue = PriorityQueue()
	visited = [False]*n
	parent = [None]*n
	queue.put((0,s))
	while not queue.empty() and visited[k]==False:
		current = queue.get()
		u=current[1]
		cost=current[0]
		visited[u]=True
		for v,w in G[u]:
			if not visited[v]:
				parent[v] = u
				queue.put((w+cost,v))

	path = [k]
	while k != s:
		path=[parent[k]]+path
		k = parent[k]
	return path


#end
