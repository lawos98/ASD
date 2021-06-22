"""
/=========================================================================================\
|Znajdowanie ilości inwersji                                                              |
|                                                                                         |
|Prosze zaproponowac i zaimplementowac algorytm, który majac na wejsciu tablice A zwraca  |
liczbe jej inwersji (t.j., liczbe par indeksów i < j takich, ze A[i] > A[j].              |
|                                                                                         |
|Algorytm oparty na Merge sort a mianowicie podczas scalania obliczamy liczbę przestawień |
|z prawej listy                                                                           |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(n)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -liczba inwersji                                    |
|                                                                                         |
\=========================================================================================/
"""

def mergesort(T):
	global counter
	if len(T) > 1:
		left = mergesort(T[0:len(T) // 2])
		right = mergesort(T[len(T) // 2:len(T)])

		mid=len(left)
		l = r = i = 0
		while l < len(left) and r < len(right):
			if left[l] <= right[r]:
				T[i] = left[l]
				l += 1
			else:
				counter+=mid-l
				T[i] = right[r]
				r += 1
			i += 1
		while l < len(left):
			T[i] = left[l]
			l += 1
			i += 1
		while r < len(right):
			T[i] = right[r]
			r += 1
			i += 1
	return T

def inversion(Array):
	global counter
	counter=0
	mergesort(Array)
	return counter


#end
