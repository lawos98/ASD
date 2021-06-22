"""
/=========================================================================================\
|Pojemniki z wodą                                                                         |
|                                                                                         |
|Mamy serie pojemników z woda, połaczonych (kazdy z kazdym) rurami.                       |
|Pojemniki maja kształty prostokatów, rury nie maja objetosci (powierzchni). Kazdy        |
|pojemnik opisany jest przez współrzedne lewego górnego rogu i prawego dolnego rogu.      |
|Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiscie woda rurami spłyneła     |
|do najnizszych pojemników). Prosze zaproponowac algorytm Obliczajacy ile pojemników      |
|zostało w pełni zalanych.                                                                |
|                                                                                         |
|Złożoność czasowa :O(log(n))             Złożoność Pamięciowa O(n)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica Krotek                            -liczba pełnych pojemników                   |
|   -poziom spodu pojemnika                                                               |
|   -poziom góry pojemnika                                                                |
|   -szerokość pojemnika                                                                  |
| -Objetość wody                                                                          |
|                                                                                         |
\=========================================================================================/
"""

def water_containers(Array,V):
	def binartSearch(Array, left, right, value):
		if left > right:
			return left
		pivot = (left + right) // 2
		if Array[pivot] == value:
			return None
		if Array[pivot] > value:
			return binartSearch(Array, left, pivot - 1, value)
		else:
			return binartSearch(Array, pivot + 1, right, value)

	def binartSearch_2(Array, left, right, value):
		if left > right:
			return right
		pivot = (left + right) // 2
		if Array[pivot] == value:
			current = binartSearch_2(Array, left, pivot - 1, value)
			if Array[current] != value:
				return pivot
			return current
		if Array[pivot] > value:
			return binartSearch_2(Array, left, pivot - 1, value)
		else:
			return binartSearch_2(Array, pivot + 1, right, value)


	n=len(Array)
	Array_levels=[]
	for i in range(n):
		index=binartSearch(Array_levels,0,len(Array_levels)-1,Array[i][0])
		if index!=None:
			Array_levels=Array_levels[:index]+[Array[i][0]]+Array_levels[index:]
		index=binartSearch(Array_levels,0,len(Array_levels)-1,Array[i][1])
		if index!=None:
			Array_levels=Array_levels[:index]+[Array[i][1]]+Array_levels[index:]

	Array_volume=[0 for _ in range(len(Array_levels)-1)]
	for i in range(n):
		j=binartSearch_2(Array_levels,0,len(Array_levels)-1,Array[i][0])
		while Array[i][1]>=Array_levels[j] and j<len(Array_levels)-1:
			if Array[i][0]<=Array_levels[j] and Array[i][1]>=Array_levels[j+1]:
				Array_volume[j]+=Array[i][2]*(Array_levels[j+1]-Array_levels[j])
			j+=1
	print(Array_volume)
	index=0
	while(V>0 and index<len(Array_volume)):
		V-=Array_volume[index]
		index+=1
	if V<0:
		index-=1

	counter=0
	for i in range(n):
		if Array[i][1]<=Array_levels[index]:
			counter+=1

    return counter


#end
