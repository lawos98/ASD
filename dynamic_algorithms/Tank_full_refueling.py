"""
/=========================================================================================\
|Minimalna liczba tankowań przy pełnym tankowaniu                                         |
|                                                                                         |
|Czołg jedzie z punktu A do punktu B. Spalanie czołgu to                                  |
|dokładnie jeden litr paliwa na jeden kilometr trasy. W baku miesci sie dokładnie         |
|L litrów paliwa. Trasa z A do B to prosta, na której znajduja sie stacje benzynowe       |
|(na pozycjach bedacych liczbami naturalnymi; A jest na pozycji 0).                       |
|Prosze podac algorytmy dla nastepujacych przypadków:                                     |
|Wyznaczamy stacje na których tankujemy tak, zeby łaczna liczba tankowan była minimalna.  |
|ale jesli na stacji tankujemy, to musimy zatankowac do pełna.                            |
|                                                                                         |
|Algorytm opiera się na programowaniu dynaminicznym a mianowice na funckji zwracającej    |
|minimalny koszt na dojechanie na pole i-te.Jest ono wyliczane w sposób poszukiwania pola |
|na którym jest stacja a nastepnie dolaniu do pełna baku oraz przemieszczenie się na      |
|wybrane pole.Oczywiście wyszukiujemy minimalych kosztów podróży                          |
|                                                                                         |
|Złożoność czasowa :O(n*k)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica stacji benzynowy           -liczba stacji do odwiedzenia                       |
| -Pojemność baku                                                                         |
|                                                                                         |
\=========================================================================================/
"""

from math import inf
def tank(Array,K):
	lenght=len(Array)
	F=[inf for _ in range(lenght)]
	Fueal=[0 for _ in range(lenght)]
	F[0]=K
	F[0]=0
	for i in range(1,lenght):
		for j in range(K):
			if F[i]>F[i-j]+Array[i-j]*(K-Fueal[i-j]) and Array[i-j]>0:
				F[i]=F[i-j]+Array[i-j]*(K-Fueal[i-j])
				Fueal[i]=K-j
	return F[lenght-1]


#end
