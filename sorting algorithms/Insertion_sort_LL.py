"""
/=========================================================================================\
|Algorytm sortowania przez wstawianie                                                     |
|                                                                                         |
|Polega na Wyciąganiu elementu i porówaniu z kolejnymi elementami zbioru posortowanego,   |
|póki nie napotkasz elementu równego lub elementu większego ,lub nie znajdziemy się       |
|na początku/końcu zbioru uporządkowanego.                                                |
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
	guardian=Node()
	guardian.next=head
	main_current_value=head.next
	head.next=None
	while(main_current_value!=None):
		current=guardian.next
		prev=guardian
		while (current!=None and current.value<main_current_value.value):
			prev=current
			current=current.next
		prev.next=main_current_value
		temp=main_current_value
		main_current_value=main_current_value.next
		temp.next=current
	return guardian.next

    
