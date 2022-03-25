"""
/=========================================================================================\
|Algorytm sortowania przez wstawianie                                                     |
|                                                                                         |
|Polega na rekurencyjnym sortowaniu danych,stosując metode (Kur)dziel i zwycieżaj         |
|A mianowicie zastowanie sortowania przez scalanie na każdej z nich odzielnie chyba że    |
|pozostał już tylko jeden element.Następnie połaczenie posortowanych ciągów               |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(n)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Operacje na wcześniej podanej Tablicy              |
|                                                                                         |
\=========================================================================================/
"""


def mergesort(T):
	if len(T) > 1:
		left = mergesort(T[0:len(T) // 2])
		right = mergesort(T[len(T) // 2:len(T)])

		l = r = i = 0
		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				T[i] = left[l]
				l += 1
			else:
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


#end
