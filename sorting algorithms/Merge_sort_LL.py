"""
/=========================================================================================\
|Algorytm sortowania przez wstawianie                                                     |
|                                                                                         |
|Polega na rekurencyjnym sortowaniu danych,stosując metode (Kur)dziel i zwycieżaj         |
|A mianowicie zastowanie sortowania przez scalanie na każdej z nich odzielnie chyba że    |
|pozostał już tylko jeden element.Następnie połaczenie posortowanych ciągów               |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(n)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""


def mergesort(head):
	if head.next == None:return head
	current=head
	guardian_left=Node()
	last_left=guardian_left
	guardian_right=Node()
	last_right=guardian_right
	while current!=None:
		last_left.next=current
		last_left=current
		current=current.next
		if current!=None:
			last_right.next=current
			last_right=current
			current=current.next
	last_left.next=None
	last_right.next=None
	left=mergesort(guardian_left.next)
	right=mergesort(guardian_right.next)

	guardian=Node()
	last=guardian
	while(left!=None and right!=None):
		if left.value<right.value:
			last.next=left
			left=left.next
		else:
			last.next=right
			right=right.next
		last=last.next
		last.next=None
	if left==None:
		last.next=right
	else:
		last.next=left

	return guardian.next


#end
