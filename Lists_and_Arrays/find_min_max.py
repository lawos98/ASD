"""
/=========================================================================================\
|Znajdowanie minimum i maksimum                                                           |
|                                                                                         |
|Prosze zaimplementowac funkcje, która majac na wejsciu tablice n elementów               |
|oblicza jednoczesnie jej najwiekszy i najmniejszy element wykonujac 1.5n porównan.       |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Minimum,Maksimum                                   |
|                                                                                         |
\=========================================================================================/
"""

def find_min_max(Array):
	n=len(Array)
	minimum=inf
	maximum=-inf
	for i in range(0,n-n%2,2):
		if Array[i]>Array[i+1]:
			if minimum>Array[i+1]:
				minimum=Array[i+1]
			if maximum<Array[i]:
				maximum=Array[i]
		else:
			if maximum<Array[i+1]:
				maximum=Array[i+1]
			if minimum>Array[i]:
				minimum=Array[i]
	return minimum,maximum


#end
