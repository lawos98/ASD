"""
/=========================================================================================\
|Sortowanie kubełkowe                                                                     |
|                                                                                         |
|Algorytm sortowania najcześciej stosowany,gdy liczby w zadanym przedziale są             |
|rozłożone jednostajnie.Idea działania polega na podzieleniu Tablicy na k podprzedziałow  |
|o równej długości,posortowaniu niepustych kubełków,a następnie wypisaniu                 |
|kolejnych kubełków                                                                       |
|W skrócie jest to counting sort po każdej pozycji w kluczach                             |
|                                                                                         |
|Złożoność czasowa                        Złożoność Pamięciowa O(n)                       |
| -rozkład jednostajny: O(n)                                                              |
| -pesymistyczna:       O(n^2)                                                            |
|Gdzie d-liczba cyft w kluczu ,k-liczba róźnych cyft                                      |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""

def Insertion_sort(Array):
	n = len(Array)
	for i in range(1, n):
		index = i - 1
		value = Array[i]
		while (index >= 0 and Array[index] > value):
			Array[index + 1] = Array[index]
			index -= 1
		Array[index + 1] = value
	return Array

def bucketSort(Array):
	size = max(Array) // len(Array)
	lenght = max(Array) // size
	Buckets = [[] for _ in range(lenght)]
	print(size,lenght,len(Array))

	for value in Array:
		index= min(value//size,lenght-1)
		Buckets[index]+=[value]

	for i in range(lenght):
		Buckets[i]=Insertion_sort(Buckets[i])

	k = 0
	for i in range(lenght):
		print(len(Buckets[i]))
		for j in range(len(Buckets[i])):
			Array[k] = Buckets[i][j]
			k += 1
	return Array


#end
