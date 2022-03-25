"""
/=========================================================================================\
|Najdłuższy wspólny podciąg                                                               |
|                                                                                         |
|Mamy dane dwie tablice, A[n] i B[n]. Nalezy znalezc                                      |
|długosc ich najdłuzszego wspólnego podciagu. (Klasyczny algorytm dynamiczny O(n2)).      |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|najwiekszy wspólny podciągu do indeksu i-tego ze zbioru A oraz j-tego.Wowczas gdy        |
|znajdziemy dwie takie same wartości zwiększamy licznik długości i-1,j-1 o jeden          |
|a wówczas gdy to nie występuje wybieramy maksymalną wartość z przedziałów zawierających  |
|albo jedną wartość mniej ze zbioru A ,albo jedną wartość mniej ze zbioru B               |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(n^2)                          |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablice A oraz B                   -Długość najdłuzszego podciagu                      |
|                                                                                         |
\=========================================================================================/
"""
def lcs(A, B):
	n = len(A)
	m = len(B)
	L = [[0 for _ in range(m+1)] for _ in range(n+1)]

	for i in range(n):
		for j in range(m):
			if A[i] == B[j]:
				L[i+1][j+1] = L[i][j] + 1
			else:
				L[i+1][j+1] = max(L[i][j+1], L[i+1][j])
	return L[n][m]


#end
