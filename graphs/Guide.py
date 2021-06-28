"""
/=========================================================================================\
|Przewodnik turystyczny                                                                   |
|                                                                                         |
|Przewodnik chce przewiezc grupe K turystów z                                             |
|miasta A do miasta B. Po drodze jest jednak wiele innych miast i miedzy róznymi miastami |
|jezdza autobusy o róznej pojemnosci. Mamy dana liste trójek postaci (x, y, c),           |
|gdzie x i y to miasta miedzy którymi bezposrednio jezdzi autobus o pojemnosci c          |
|pasazerów. Przewodnik musi wyznaczyc wspólna trase dla wszystkich tursytów i musi ich    |
|podzielic na grupki tak, zeby kazda grupka mogła przebyc trase bez rodzielania sie.      |
|Prosze podac algorytm, który oblicza na ile (najmniej) grupek przewodnik musi podzielic  |
|turystów (i jaka trasa powinni sie poruszac), zeby wszyscy dostali sie z A do B.         |
|                                                                                         |
|Algorytym opiera się na algorytmie Dikstry w którym relaksacja odbywa się poprzez        |
|zwieszanie liczby pasażerow na danej trasie                                              |
|                                                                                         |
|Złożoność czasowa :O(E*log(V))      Złożoność Pamięciowa O(E*log(V)) )                   |
|                                                                                         |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Macierz sąsiedztwa                 -Liczba grup                                        |
| -punkt startowy                     -Maksymalna ścieżka                                 |
| -punkt końcowy                                                                          |
| -liczba uczestników                                                                     |
|                                                                                         |
\=========================================================================================/
"""

from queue import PriorityQueue
from math import inf


def Guide(Graph,s,k,T):
	def Dikstry(Array, s,k):
		n = len(Array)
		d = [-inf] * n
		parent = [-1] * n
		d[s] = inf
		Q = PriorityQueue()
		Q.put([d[s], s])
		while not Q.empty():
			u = Q.get()
			u = u[1]
			for v, w in Array[u]:
				if d[v]<min(d[u],w) and w>0:
					d[v] = min(d[u],w)
					Q.put([d[v], v])
					parent[v] = u
		Result=[]
		index=k
		while index!=s:
			Result=[index]+Result
			index=parent[index]
		Result=[s]+Result
		return Result,d[k]

	current=Dikstry(Graph,s,k)
	Path=current[0]
	people=current[1]
	counter=0
	while T>0:
		counter+=1
		T-=people
	print(counter)
	print(Path)


#end
