"""
/=========================================================================================\
|Spadające bloczki                                                                        |
|                                                                                         |
|                                                                                         |
|Kazdy klocek to przedział postaci [a, b]. Dany jest ciag klocków [a1, b1],               |
|[a2, b2], . . ., [an, bn]. Klocki spadaja na os liczbowa w kolejnosci podanej w ciagu.   |
|Prosze zaproponowac algorytm, który oblicza ile klocków nalezy usunac z listy tak,       |
|zeby kazdy kolejny spadajacy klocek miescił sie w całosci w tam, który spadł             |
|tuz przed nim.                                                                           |
|                                                                                         |
|Algorytm opiera się na LIS a mianowicie szukamy takie ciągu że pierwsza współrzedna      |
|jest większa bądź równa od poszukiwanej, a druga jest mniejsza bądź równa od             |
|poszukiwanej.Następnie po obliczeniu maksymalnej wierzy wystarczy odjąć nasz wynik od    |
|wszystkich klocków aby otrzymać liczbę klocków do usunieica                              |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Liczba klocków do usuniecia                        |
|                                                                                         |
\=========================================================================================/
"""
def lis(Array):
	n = len(Array)
	f=[1 for _ in range(n)]
	for i in range(1, n):
		for j in range(i):
			if Array[j][0] <= Array[i][0] and  Array[j][1] >= Array[i][1] and f[i]<f[j]+1:
				f[i] = f[j] + 1

	return n-max(f)


def faling_blocks(Array):
	return lis(Array)


#end
