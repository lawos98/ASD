"""
/=========================================================================================\
|Odwracanie listy                                                                         |
|                                                                                         |
|Prosze zaimplementowac funkcje odwracajaca liste jednokierunkowa.                        |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""

class Node:
	def __init__(self,value=None):
		self.next = None
		self.value = value

def reverse_LL(root):
	guardian=Node()
	while root!=None:
		temp=root.next
		root.next=guardian.next
		guardian.next=root
		root=temp
	return guardian.next


#end
