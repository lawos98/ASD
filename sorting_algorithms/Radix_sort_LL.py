"""
/=========================================================================================\
|Sortowanie pozycyjne                                                                     |
|                                                                                         |
|Algorytm sortowania porządkujący stabilnie ciągi wartości (liczb, słów) względem         |
|konkretnych cyfr, znaków itp, kolejno od najmniej znaczących do najbardziej              |
|znaczących pozycji                                                                       |
|W skrócie jest to counting sort po każdej pozycji w kluczach                             |
|                                                                                         |
|Złożoność czasowa :O(d(n+k))             Złożoność Pamięciowa O(n+k)                     |
|Gdzie d-liczba cyft w kluczu ,k-liczba róźnych cyft                                      |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
| -system liczbowy                                                                        |
\=========================================================================================/
"""

def sort_by_digit(Head, system, digit_number):
	def get_number(Head, system, digit_number):
		value = Head.value
		for _ in range(digit_number):
			value //= system
		return value % system

	Array_Guardian= [Node() for _ in range(system)]
	Array_Last=[-1]*system
	for i in range(system):
		Array_Last[i]=Array_Guardian[i]

	while Head!=None:
		index=get_number(Head,system,digit_number)
		last=Array_Last[index]
		last.next=Head
		Head=Head.next
		last=last.next
		Array_Last[index]=last
	guardian=Node()
	last=guardian
	for i in range(system):
		start=Array_Guardian[i]
		start=start.next
		if start!=None:
			last.next=start
			last=Array_Last[i]
	last.next=None
	return guardian.next
def radix_sort(head,system):
	current=head
	maximum=head.value
	current=current.next
	while current!=None:
		if maximum<current.value:
			maximum=current.value
		current=current.next
	digits=0
	while maximum>0:
		maximum//=system
		digits+=1
	for i in range(digits):
		head=sort_by_digit(head,system,i)
	return head


#end
