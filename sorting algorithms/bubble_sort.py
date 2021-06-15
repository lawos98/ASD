"""
/=========================================================================================\
|Algorytm sortowania Babelkowego                                                          |
|                                                                                         |
|Polega na porównywaniu dwóch kolejnych elementów i zamianie ich kolejności               |
|jeżeli zaburza ona porządek, w jakim się sortuje tablicę. Sortowanie kończy się,         |
|gdy podczas kolejnego przejścia nie dokonano żadnej zmiany.                              |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Operacje na wcześniej podanej Tablicy              |
|                                                                                         |
\=========================================================================================/
"""

def Bubble_sort(Array):
	Flag=1
	while(Flag):
		Flag=0
		for index in range(1,len(Array)):
			if Array[index]<Array[index-1]:
				Array[index],Array[index-1]=Array[index-1],Array[index]
				Flag=1


#end
