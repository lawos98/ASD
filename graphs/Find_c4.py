"""
/=========================================================================================\
|Znajdowanie Cyklu o długości 4                                                           |
|                                                                                         |
|Dany jest graf nieskierowany G zawierajacy n wierzchołków. Zaproponuj                    |
|algorytm, który stwierdza czy w G istnieje cykl składajacy sie z dokładnie               |
|4 wierzchołków. Zakładamy, ze graf reprezentowany jest przez macierz sasiedztwa A.       |
|                                                                                         |
|Algorytm ma na celu znalezienie cyklu o długości 4.Na początku przechodzimy wszystkie    |
|wierzchołki sprawdzając czy możemy z danego wierzchołka dojść do wierzchołka             |
|oddalonego o 2 krawędzię na dwa sposoby blokując przy tym podróż do naszego wierzchołka  |
|początkowego aby nie powstał nam cykl wracający po własnych krawędziach                  |
|(korzenia drzewa).Zapamietując przy tym dany wierzchołek poprzedzający                   |
|                                                                                         |
|Złożoność czasowa :             Złożoność Pamięciowa O(V)                                |
| -graf rzadki: O(V)                                                                      |
| -graf pełny : O(V^3)                                                                    |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Aktualna kolejność usuwanie sieci                  |
|                                                                                         |
\=========================================================================================/
"""

def cycle(graph):
	def bfs(graph, s):

		number_path = [0]*len(graph)
		previous = [None]*len(graph)

		q=deque()
		number_path[s]=-1
		for v in graph[s]:
			q.append(v)

		while len(q)!=0:
			u=q.popleft()
			for v in graph[u]:
				if number_path[v]!=-1:
					number_path[v]+=1
					if number_path[v]==2:
						t=[u,v,previous[v]]
						return t
					previous[v]=u
		return False


	for v in range(len(graph)):
		c=bfs(graph,v)
		if c!=False:
			c=[v]+c+[v]
			return c
	return None


#end
