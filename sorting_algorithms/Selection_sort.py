"""
/=========================================================================================\
|Algorytm sortowania przez wybieranie                                                     |
|                                                                                         |
|Polega na wyszukaniu elementu mającego się znaleźć na żądanej pozycji i zamianie         |
|miejscami z tym, który jest tam obecnie. Operacja jest wykonywana dla wszystkich         |
|indeksów sortowanej tablicy.                                                             |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Operacje na wcześniej podanej Tablicy              |
|                                                                                         |
\=========================================================================================/
"""

def Insertion_sort(Array):
	n=len(Array)
	for i in range(n):
		max_index=i
		for j in range(i+1,n):
			if Array[j]<Array[max_index]:
				max_index=j
		Array[max_index],Array[i]=Array[i],Array[max_index]


#end
