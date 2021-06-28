"""
/=========================================================================================\
|DObry początek                                                                           |
|                                                                                         |
|Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli                      |
|kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac    |
|algorytm, który stwierdza czy dany graf zawiera dobry poczatek                           |
|                                                                                         |
|Algorytym opiera się na znalezieniu za pomocą DFS wierzchołka który nie posiada rodzica  |
|wraz z wykluczonymi wierzchołkami (zapobiega cyklowi).Następnie sprwdzamy również za     |
|pomocą DFS czy z danego wierzchołka można odwiedzić wszystkie wierzchołki                |
|                                                                                         |
|Złożoność czasowa :O(V)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Macierz sąsiedztwa                 -Stwierdzenie czy istnieje omawiany wierzchołek     |
|                                                                                         |
\=========================================================================================/
"""

def good_start(Graph):
	def dfs_visit_reverse(u):
		nonlocal Graph, visited
		visited[u] = True
		for v in range(len(Graph)):
			if not visited[v] and Graph[v][u]==1:
				return dfs_visit_reverse(v)
		return u
	def dfs_visit(u):
		nonlocal Graph, visited,vertex
		vertex=u
		visited[u] = True
		for v in range(len(Graph)):
			if not visited[v] and Graph[u][v]==1:
				dfs_visit(v)

	visited = [False for _ in range(len(Graph))]
	vertex=dfs_visit_reverse(0)
	print(vertex)
	visited = [False for _ in range(len(Graph))]
	dfs_visit(vertex)
	for i in range(len(visited)):
		if visited[i]==False:return False
	return True


#end
