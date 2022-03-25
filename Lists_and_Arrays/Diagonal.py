"""
/=========================================================================================\
|Przekątna                                                                                |
|                                                                                         |
|Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi      |
|(liczby są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca   |
|tablicę T, tak aby elementy leżące pod główną przekątną nie były większe od elementów    |
|na głównej przekątnej, a elementy leżące nad główną przekątną nie były mniejsze od       |
|elementów na głównej przekątnej.Algorytm powinien być jak najszybszy oraz używać jak     |
|najmniej pamięci ponad tę, która potrzebna jest na przechowywanie danych wejściowych     |
|(choć algorytm nie musi działać w miejscu). Proszę podać złożoność czasową i pamięciową  |
|zaproponowanego algorytmu.                                                               |
|                                                                                         |
|Algorytm opiera się na odnalezieniu przedziału(quicksort) znajdującego się na przekątnej |
|przestawienu go tam a następnie podmianie wartości mniejszych znajdujących się nad       |
|przekątną z wartościami wiekszymi znajdujących nad przekątną,jest ich parzysta ilość     |
|więc spokojnie możemy zamieniać miejscami                                                |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(1)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""

def swap(Array,index1,index2,lenght):
	Array[index1//lenght][index1%lenght],Array[index2//lenght][index2%lenght]=Array[index2//lenght][index2%lenght],Array[index1//lenght][index1%lenght]

def partition(Array, left, right,lenght):
	x = Array[right//lenght][right%lenght]
	i = left - 1
	for j in range(left, right):
		if Array[j//lenght][j%lenght] <= x:
			i += 1
			swap(Array,i,j,lenght)
	swap(Array,i+1,right,lenght)
	return i + 1

def kthSmallest(arr, l, r, k,lenght):
	if (k > 0 and k <= r - l + 1):
		index = partition(arr, l, r,lenght)
		if (index - l == k - 1):
			return index
		if (index - l > k - 1):
			return kthSmallest(arr, l, index - 1, k,lenght)
		return kthSmallest(arr, index + 1, r, k - index + l - 1,lenght)
	return -1

def diagonal(Array):
	n=len(Array)
	diagonal_start=0
	for i in range(n):
		diagonal_start+=i
	kthSmallest(Array,0,n*n-1,diagonal_start,n)
	kthSmallest(Array,0,n*n-1,diagonal_start+n-1,n)
	index_diagonal=0
	for i in range(diagonal_start,diagonal_start+n):
		swap(Array,i,index_diagonal,n)
		index_diagonal+=1+n
	index_lower=n*(n-1)
	index_lower_current=index_lower
	index_upper=n-1
	index_upper_current=index_upper
	while index_lower_current!=0 or index_upper_current!=0:
		while Array[index_lower_current//n][index_lower_current%n]<=Array[0][0] and index_lower_current!=0:
			if index_lower_current//n==n-1:
				index_lower-=n
				index_lower_current=index_lower
			else:
				index_lower_current+=n+1
		while Array[index_upper_current//n][index_upper_current%n]>Array[0][0] and index_upper_current!=0:
			if index_upper_current%n==n-1:
				index_upper-=1
				index_upper_current=index_upper
			else:
				index_upper_current+=n+1
		swap(Array,index_upper_current,index_lower_current,n)


#end
