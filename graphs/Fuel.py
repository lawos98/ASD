"""
/=========================================================================================\
|Problem stacji benzynowych na grafie                                                     |
|                                                                                         |
|Pewien podróznik chce przebyc trase z punktu A                                           |
|do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr  |
|trasy.Wbaku miesci sie dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf,   |
|gdzie wierzchołki to miasta a krawedzie to łaczace je drogi. Kazda krawedz ma długosc w  |
|kilometrach (przedstawiona jako licza naturalna). W kazdym wierzchołku jest stacja       |
|benzynowa, z dana cena za litr paliwa. Prosze podac algorytm znajdujacy trase z punktu   |
|A do punktu B o najmniejszym koszcie. Prosze uzasadnic poprawnosc algorytmu.             |
|                                                                                         |
|Algorytym opiera się na algorytmie Dikstry w którym relaksacja oblicza odległość co      |
|drugiej krawędzi.Co za tym idzie algorytm najpierw wylicza w przypadku gdy nasz kierowca |
|zaczyna trase jak i w sytuacji kiedy jest drugi                                          |
|                                                                                         |
|Złożoność czasowa :O(f*E*log(V))      Złożoność Pamięciowa O(f*E*log(V)) )               |
| -gdzie f to pojemność baku                                                              |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Listwa sąsiedztwa                  -Koszt objazdu                                      |
| -punkt startowy                     -Trasa przejazdu                                    |
| -punkt końcowy                                                                          |
| -Ceny paliw na stacjach                                                                 |
| -pojemnośc baku                                                                         |
|                                                                                         |
\=========================================================================================/
"""

from math import inf
from queue import PriorityQueue


def Dikstry(Array, Prices, s,k, fuel):
	n = len(Array)
	C = [inf] * n
	parent = [-1] * n
	C[s] = 0
	Q = PriorityQueue()
	Q.put([C[s], 0, s])
	while not Q.empty():
		cost,f,u=Q.get()
		tank = fuel
		price = Prices[u]*(fuel-f)
		for i in range(fuel,f-1,-1):
			for v, w in Array[u]:
				if w<=tank and cost+price<C[v]:
					C[v] = cost + price
					parent[v] = u
					Q.put([cost+price,tank-w, v])
			price -= Prices[u]
			tank -= 1
	index=k
	Result=[]
	while index!=s:
		Result=[index]+Result
		index=parent[index]
	Result=[s]+Result
	print(C)
	return Result,C[k]
