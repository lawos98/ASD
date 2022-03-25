"""
/=========================================================================================\
|Sortowanie kubełkowe                                                                     |
|                                                                                         |
|Algorytm sortowania najcześciej stosowany,gdy liczby w zadanym przedziale są             |
|rozłożone jednostajnie.Idea działania polega na podzieleniu Tablicy na k podprzedziałow  |
|o równej długości,posortowaniu niepustych kubełków,a następnie wypisaniu                 |
|kolejnych kubełków                                                                       |
|W skrócie jest to counting sort po każdej pozycji w kluczach                             |
|                                                                                         |
|Złożoność czasowa                        Złożoność Pamięciowa O(n)                       |
| -rozkład jednostajny: O(n)                                                              |
| -pesymistyczna:       O(n^2)                                                            |
|Gdzie d-liczba cyft w kluczu ,k-liczba róźnych cyft                                      |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""

def Insert_to_bucket(guardian,newNode):
	prev=guardian
	current=guardian.next
	if current==None:
		guardian.next=newNode
		newNode.next=None
		return guardian
	while current!=None and newNode.value>current.value:
		prev=current
		current=current.next
	prev.next=newNode
	newNode.next=current
	return guardian


def bucketSort(head):
	current = head
	maximum = head.value
	lenght = 1
	current = current.next

	while current != None:
		lenght += 1
		if maximum < current.value:
			maximum = current.value
		current = current.next

	size = maximum // lenght
	Bucket_number = maximum // size
	Buckets_guardian = [Node() for _ in range(Bucket_number)]
	current = head

	while current != None:
		index = min(current.value // size, Bucket_number - 1)
		temp=current.next
		Buckets_guardian[index]=Insert_to_bucket(Buckets_guardian[index],current)
		current=temp

	for i in range(Bucket_number):
		start=Buckets_guardian[i]
		start=start.next
		if start==None:continue

	current=Buckets_guardian[0]
	while current.next!=None:
		current=current.next
	last=current

	for i in range(1,Bucket_number):
		current=Buckets_guardian[i]
		current=current.next
		if current!=None:
			last.next=current
			while current.next!=None:
				current=current.next
			last=current

	guardian=Buckets_guardian[0]
	return guardian.next


#end
