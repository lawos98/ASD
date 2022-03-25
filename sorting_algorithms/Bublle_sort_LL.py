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
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""


def Buble_sort_LL(head):
	if head.next==None:return
	guardian=Node()
	guardian.next=head
	Flag=1
	while(Flag):
		Flag=0
		prev=guardian.next
		current=prev.next
		if current.value<prev.value:
			guardian.next=current
			prev.next=current.next
			current.next=prev
			Flag=1
		while(current!=None):
			if current.next!=None and current.next.value<current.value:
				prev.next=current.next
				temp=current.next
				current.next=temp.next
				temp.next=current
				Flag=1
			prev=current
			current=current.next
	return guardian.next


#end
