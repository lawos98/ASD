"""
/=========================================================================================\
|Minimalny koszt przeniesienia króla                                                      |
|                                                                                         |
|Dana jest szachownica o wymiarach n × n. Kazde pole (i, j)                               |
|ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A                       |
|(na polu A[j][i]). W lewym górnym rogu szachownicy stoi król, którego zadaniem           |
|jest przejsc do prawego dolnego rogu, przechodzac po polach o minmalnym sumarycznym      |
|koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt               |
|sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.                              |
|                                                                                         |
|Algorytm opiera się na BFS a mianowicie przechodząc do następnego wierzchołka który ma   |
|zapisując jego aktualny koszt natrafiając na nieodwiedzone pole zapisujemy jego koszt    |
|dojścia na owe pole,lub gdy natrafimy na pole w którym możemy zmiejszyć koszt przejścia  |
|                                                                                         |
|Złożoność czasowa :O(n^2)             Złożoność Pamięciowa O(n^2)                        |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Macierz pól na szachownicy         -Minimalna ścieżka                                  |
|                                                                                         |
\=========================================================================================/
"""
def king(graph):
	n=len(graph)
	queue = PriorityQueue()
	visited = [[False for _ in range(n)]for _ in range(n)]
	costen = [[-1 for _ in range(n)]for _ in range(n)]
	parent = [[-1 for _ in range(n)]for _ in range(n)]
	queue.put((0,0,0))
	costen[0][0]=graph[0][0]
	vectors=[[-1,0],[1,0],[0,-1],[0,1]]
	while not queue.empty():
		current = queue.get()
		x=current[0]
		y=current[1]
		for v_1,v_2 in vectors:
			if 0<=x+v_1<n and 0<=y+v_2<n:
				if visited[x+v_1][y+v_2]==False or costen[x+v_1][y+v_2]>costen[x][y]+graph[x+v_1][y+v_2]:
					parent[x+v_1][y+v_2]=[x,y]
					costen[x+v_1][y+v_2]=costen[x][y]+graph[x+v_1][y+v_2]
					visited[x+v_1][y+v_2]=True
					queue.put((x+v_1,y+v_2))

	x=n-1
	y=n-1
	path = []
	while x!=0 or y!=0:
		path=[(x,y)]+path
		x,y=parent[x][y]
	path=[(0,0)]+path
	return path


#end
