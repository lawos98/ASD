"""
/=========================================================================================\
|Sprawdzanie czy w drzewie istnieje ścieżka Hamiltiona                                    |
|                                                                                         |
|Sciezka Hamiltona to sciezka przechodzaca przez wszystkie                                |
|wierzchołki w grafie, przez kazdy dokładnie raz. W ogólnym grafie znalezienie            |
|sciezki Hamiltona jest problemem NP-trudnym. Prosze podac algorytm, który stwierdzi      |
|czy istnieje sciezka Hamiltona w acyklicznym grafie skierowanym.                         |
|                                                                                         |
|Algorytm ma za zadanie sprawdzić czy dane drzewo jest ściezką a wiec wyszukujemy pierwszy|
|liść w drzewie i przechodzimy do drugiego sprawdzając czy nie istnieje wierzchhołek      |
|przekraczający stopień dwa który dyskalifikuje nasze drzewo                              |
|                                                                                         |
|Złożoność czasowa :O(V)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Lista sąsiedztwa                   -Stwierdzenie czy jest to ścieżka Hamiltona         |
|                                                                                         |
\=========================================================================================/
"""

def Hamiltonian_path_in_tree(Graph):
	def go_to_end():
		nonlocal u,parent,Graph
		edges=len(Graph[u])
		while edges!=1:
			if edges!=2:
				return False
			if Graph[u][0]!=parent:next=Graph[u][0]
			elif Graph[u][1]!=parent:next=Graph[u][1]
			parent=u
			u=next
			edges=len(Graph[u])
		return True

	n=len(Graph)
	if len(Graph[0])!=1:
		parent=-1
		u=0
		if not go_to_end():return False
		parent,u=u,parent
	else:
		parent=0
		u=Graph[0][0]
	if not go_to_end():return False
	return True


#end
