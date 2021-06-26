"""
/=========================================================================================\
|Minimalna koszt tankowań                                                                 |
|                                                                                         |
|Czołg jedzie z punktu A do punktu B. Spalanie czołgu to                                  |
|dokładnie jeden litr paliwa na jeden kilometr trasy. W baku miesci sie dokładnie         |
|L litrów paliwa. Trasa z A do B to prosta, na której znajduja sie stacje benzynowe       |
|(na pozycjach bedacych liczbami naturalnymi; A jest na pozycji 0).                       |
|Prosze podac algorytmy dla nastepujacych przypadków:                                     |
|Wyznaczamy stacje tak, zeby koszt przejazdu był minimalny (w tym wypadku                 |
|kazda stacja ma dodatkowo cene za litr paliwa). Na kazdej stacji mozemy                  |
|tankowac dowolna ilosc paliwa.                                                           |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie na zmieniemu pola na            |
|na najstańsze pole w aktualnym zasięgu wraz z aktualnym polu lub jeżeli bak jest pełen   |
|bez aktualnego pola,jeżeli jest możliwość przemieszczenia na ostatnie pole na            |
|aktualnym baku,jest to zakończenie algorytmu
|                                                                                         |
|Złożoność czasowa :O(n*k)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica stacji benzynowy           -liczba stacji do odwiedzenia                       |
| -Pojemność baku                                                                         |
|                                                                                         |
\=========================================================================================/
"""

from random import randint
from math import inf
def tank(Array,K):
	def find_min(Array,index,fueal):
		min_index=inf
		for i in range(index,index+fueal+1):
			if Array[i]!=0:
				min_index=i
		if min_index==inf:return -1
		for i in range(index,index+fueal+1):
			if Array[i]<=Array[min_index] and Array[i]>0:
				min_index=i
		return min_index

	lenght=len(Array)
	index=0
	costs=0
	fueal=0
	if Array[index]>0:
		costs+=Array[index]
		fueal=1
	else:
		return -1
	while index!=lenght-1 and fueal!=0:
		if index+fueal>=lenght-1:
			fueal-=lenght-1-index
			index=lenght-1
			break
		if fueal==K:
			index_to_go=find_min(Array,index+1,fueal-1)
			if index_to_go==-1:
				return -1
		else:
			index_to_go=find_min(Array,index,fueal)
		costs+=Array[index_to_go]
		fueal-=index_to_go-index
		fueal+=1
		index=index_to_go
	return costs
