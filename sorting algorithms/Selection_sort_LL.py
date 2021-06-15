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
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""



def Insertion_sort_LL(head):
	if head.next==None:return
	guardian_input=Node()
	guardian_output=Node()
	guardian_input.next=head
	last=guardian_output
	while(guardian_input.next!=None):
		current=guardian_input.next
		min_value=current.value
		current=current.next
		while(current!=None):
			if current.value<min_value:
				min_value=current.value
			current=current.next
		current=guardian_input.next
		prev=guardian_input
		while (current.value!=min_value):
			prev=current
			current=current.next
		prev.next=current.next
		last.next=current
		last=current
		current.next=None
	return guardian_output.next

    
