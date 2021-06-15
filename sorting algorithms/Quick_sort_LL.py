"""
/=========================================================================================\
|Algorytm sortowania szybkiego                                                            |
|                                                                                         |
|Polega na wybraniu elementu rozdzielającego,a następnie tablica jest dzielona na dwa     |
|fragmenty do początkowego przenoszone są wszystkie elementy nie większe od               |
|rozdzielającego, do końcowego wszystkie większe.Potem sortuje się osobno początkową      |
|i końcową część tablicy.Rekursja kończy się, gdy kolejny fragment uzyskany z podziału    |
|zawiera pojedynczy element, jako że jednoelementowa tablica nie wymaga sortowania.       |
|pozostał już tylko jeden element.Następnie połaczenie posortowanych ciągów               |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(log(n))(Tail Call)       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""

def qsort(L):
	if L == None or L.next == None:
		return L

	wartownik = Node()
	wartownik.next = L
	pivot = L
	less = wartownik
	more = L
	curent = L.next

	while curent != None:
		if curent.value < pivot.value:
			less.next = curent
			less = curent
		else:
			more.next = curent
			more = curent
		curent = curent.next

	more.next = None
	less.next = None

	Less_tab = qsort(wartownik.next)
	More_tab = qsort(pivot.next)

	if Less_tab == None:
		pivot.next = More_tab
		return pivot
	wartownik.next = Less_tab
	while Less_tab != None and Less_tab.next != None:
		Less_tab = Less_tab.next
	Less_tab.next = pivot
	pivot.next = More_tab

	return wartownik.next


#end
