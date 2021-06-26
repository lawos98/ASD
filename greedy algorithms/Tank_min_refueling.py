"""
/=========================================================================================\
|Minimalna liczba tankowań                                                                |
|                                                                                         |
|Czołg jedzie z punktu A do punktu B. Spalanie czołgu to                                  |
|dokładnie jeden litr paliwa na jeden kilometr trasy. W baku miesci sie dokładnie         |
|L litrów paliwa. Trasa z A do B to prosta, na której znajduja sie stacje benzynowe       |
|(na pozycjach bedacych liczbami naturalnymi; A jest na pozycji 0).                       |
|Prosze podac algorytmy dla nastepujacych przypadków:                                     |
|Wyznaczamy stacje na których tankujemy tak, zeby łaczna liczba tankowan była minimalna.  |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie na zmieniemu pola na            |
|najbardziej oddaloną stację aż do momentu gdzie dotrzemy do miejsca gdzie nie możemy     |
|dalej się przemieszczać albo dotrzemy do końca Tablicy                                   |
|                                                                                         |
|Złożoność czasowa :O(n*k)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica stacji benzynowy           -liczba stacji do odwiedzenia                       |
| -Pojemność baku                                                                         |
|                                                                                         |
\=========================================================================================/
"""

def tank(Array,K):
	index=0
	if Array[index]>0:
		fueal=K
		counter=1
	else:
		fueal=0
		counter=0
	lenght=len(Array)
	while index!=lenght-1 and fueal!=0:
		if index+fueal>=lenght-1:
			index=lenght-1
			break
		index_to_go=index
		for i in range(index,index+fueal+1):
			if Array[i]>0:
				index_to_go=max(index_to_go,i)
		if index!=index_to_go:
			fueal=K
			counter+=1
		else:
			fueal=0
		index=index_to_go
	if index!=lenght-1:
		return -1
	else:
		return counter


#end
