"""
/=========================================================================================\
|Sortowania przez kopcowanie                                                              |
|                                                                                         |
|Algorytm składa się z dwóch faz. W pierwszej sortowane                                   |
|elementy reorganizowane są w celu utworzenia kopca. W drugiej zaś dokonywane             |
|jest właściwe sortowanie.                                                                |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(n)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Operacje na wcześniej podanej Tablicy              |
|                                                                                         |
\=========================================================================================/
"""

def get_value(A,index):
	node=A[index]
	return node.value

def swap(A,index1,index2):
	A[index1],A[index2]=A[index2],A[index1]

def get_Array(root):
	A=[]
	while root!=None:
		A+=[root]
		root=root.next
	return A

def get_LL(A):
	guardian=Node()
	last=guardian
	for i in A:
		last.next=i
		last=i
	return guardian.next

def heapify(A, n, i):
	l = 2 * i + 1
	r = 2 * i + 2
	m = i
	if l < n and get_value(A,l)>get_value(A,m):
		m = l
	if r < n and get_value(A,r)>get_value(A,m):
		m = r
	if m != i:
		swap(A,i,m)
		heapify(A, n, m)

def buildheap(A):
	n = len(A)
	for i in range(n, -1, -1):
		heapify(A, n, i)

def heapsort(root):
	A=get_Array(root)
	n = len(A)
	buildheap(A)
	for i in range(n - 1, 0, -1):
		swap(A,0,i)
		heapify(A, i, 0)
	return get_LL(A)


#end
