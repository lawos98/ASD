"""
/=========================================================================================\
|uniwersalne ujście                                                                       |
|                                                                                         |
|Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym                          |
|ujsciem, jesli (a) z kazdego innego wierzchołka v istnieje krawedz z v do t, oraz        |
|(b) nie istnieje zadna krawedz wychodzaca z t.                                           |
|                                                                                         |
|Algorytm opiera się na przechodzeniu do nastepnego wierzchołka kiedy to możliwe          |
|a następnie sprawdzeniu tego iwerzchołka czy Wszystkie wierzchołki do niego prowadzą     |
|oraz sprawdzeniu czy nie istnieje krawedź prowadząca z owego wierzchołka do innego       |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Macierz sąsiedztwa                 -wierzchołek bedący uniwersalnym ujście             |
|                                                                                         |
\=========================================================================================/
"""
def uniwersalne(G):
	n = len(G)
	index = 0
	for i in range(n):
		if G[index][i]:
			print(index,end="-> ")
			index = i
			print(index)

	for i in range(n):
		if i != index and G[i][index] == 0:
			return False
		if G[index][i] == 1:
			return False

	return index
