"""
/=========================================================================================\
|Scieżka zawierająca malejące krawędzie                                                   |
|                                                                                         |
|Dany jest graf G = (V,E), którego wierzchołki reprezentuja punkty                        |
|nawigacyjne nad Bajtocja, a krawedzie reprezentuja korytarze powietrzne miedzy           |
|tymi punktami. Kazdy korytarz powietrzny ei > E powiazany jest z optymalnym pułapem      |
|przelotu pi > N (wyrazonym w metrach).Przepisy dopuszczaja przelot danym korytarzem      |
|jesli pułap samolotu rózni sie od optymalnego najwyzej o t metrów.                       |
|Prosze zaproponowac algorytm (bez implementacji), który sprawdza czy istnieje            |
|mozliwosc przelotu z zadanego punktu x > V do zadanego punktu y > V w taki sposób,       |
|zeby samolot nigdy nie zmieniał pułapu.Algorytm powinien byc poprawny i mozliwie jak     |
|najszybszy. Prosze oszacowac jego złozonosc czasowa.                                     |
|                                                                                         |
|Algorytm opiera się na DFS a mianowicie przechodząc do następnego wierzchołka który ma   |
|nie był przez nas odwiedzony i ograniczamy jego maksymalna i minimalną wysokośc          |
|przelotu jeżeli z wierzchołka nie jesteśmy w stanie przelecieć na aktualnym pułapie      |
|jest on wykreślany z odiwedzonym i jego pułap jest nadpisywany nowym                     |
|                                                                                         |
|Złożoność czasowa :O(V*E)             Złożoność Pamięciowa O(V)                          |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Ścieżka z s to k                                   |
| -Wierzchołek startowy               -Minimalny pułap z jakim można przelecieć trase     |
| -Wierzchołek końcowy                -Maksymalny pułap z jakim można przelecieć trase    |
| -Różnica pułapu                                                                         |
|                                                                                         |
\=========================================================================================/
"""
from math import inf
def dfs(graph,s,k,T):
	visited = [False for _ in range(len(graph))]
	Parent=[-1 for _ in range(len(graph))]
	Min_height= [-inf for _ in range(len(graph))]
	Max_height= [inf for _ in range(len(graph))]
	def dfs_visit(u):
		nonlocal graph,Min_height,Max_height,T,k
		visited[u] = True
		if u==k:
			return 1
		for v,h in graph[u]:
			if not visited[v] and Min_height[u]<=h<=Max_height[u]:
				Parent[v]=u
				Min_height[v] = max(Min_height[u], h - T)
				Max_height[v] = min(Max_height[u], h + T)
				if dfs_visit(v):
					return 1
		visited[u]=False

	dfs_visit(s)
	path = [k]
	u=k
	while u != s:
		path=[Parent[u]]+path
		u = Parent[u]
	return path,Min_height[k],Max_height[k]


#end
