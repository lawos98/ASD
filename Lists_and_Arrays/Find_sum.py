"""
/=========================================================================================\
|Znajdowanie dwóch elementów o określonej sumie                                           |
|                                                                                         |
|Dana jest posortowana tablica A[1...n] oraz liczba x. Prosze napisac program,            |
|który stwierdza czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x.                 |
|                                                                                         |
|Algorytm opiera się na stworzeniu okna a nastepnie modelujemy jego szerokość odpowiednio |
|jeżeli suma krańcowych wyrazów okna jest większe od szukanej wartości przesuwamy         |
|prawy kraniec okna w lewo,natomiast jeżeli jest mniejsza lewy kraniec okna w prawo       |
|jeżeli do momentu znikniecia okna nie znajdziemy naszej wartości oznacza to że nie       |
|istnieje owa suma                                                                        |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(1)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -indeksy owej sumy                                  |
|                                                                                         |
\=========================================================================================/
"""



def find_sum(Array,value):
	n=len(Array)
	left=0
	right=n-1
	while right!=left:
		if Array[left]+Array[right]==value:
			return left,right
		if Array[left]+Array[right]<value:
			left+=1
		if Array[left]+Array[right]>value:
			right-=1
	return -1


#end
