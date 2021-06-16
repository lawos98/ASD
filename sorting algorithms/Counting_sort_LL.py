"""
/=========================================================================================\
|Algorytm sortowania przez zliczanie                                                      |
|                                                                                         |
|Na początku działania algorytmu ustalany jest przedział wartości, które zależą od        |
|wartości wszystkich elementów w sekwencji, która ma być posortowana                      |
|Dla każdego elementu z utworzonego przedziału obliczana jest ilość jego wystąpień        |
|w wejściowej sekwencji.Następny krok polega na analizie wszystkich elementów listy       |
|zliczającej. i-tą liczbę na liście wypisujemy tyle razy jaką wartość ma lista pod        |
|indeksem i. W ten sposób uzyskujemy posortowaną listę. Jeśli listę zliczającą            |
|będziemy przeglądać od lewej do prawej to uzyskamy listę posortowaną rosnącą.            |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""

def counting_sort(head):
	guardian=Node()
	guardian.next=head
	current=head
	minimum=head.value
	maximum=head.value
	current=current.next
	while(current!=None):
		if (current.value<minimum):minimum=current.value
		elif(current.value>maximum):maximum=current.value
		current=current.next
	lenght=maximum-minimum+1
	Guardian_Array=[Node() for _ in range(lenght)]
	Last=[None]*lenght
	for i in range(lenght):
		Last[i]=Guardian_Array[i]
	current=guardian.next
	while(current!=None):
		index=current.value-minimum
		Last_Node=Last[index]
		Last_Node.next=current
		Last[index]=current
		current=current.next
	last=guardian
	for i in range(lenght):
		start=Guardian_Array[i]
		if(start.next!=None):
			last.next=start.next
			last=Last[i]
	last.next=None
	return guardian.next
