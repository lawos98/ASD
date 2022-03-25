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

def heapify(A,n,i):
    l=2*i+1
    r=2*i+2
    m=i
    if l<n and A[l]>A[m]:
        m=l
    if r<n and A[r]>A[m]:
        m=r
    if m!=i:
        A[i],A[m]=A[m],A[i]
        heapify(A,n,m)

def buildheap(A):
    n=len(A)
    for i in range(n,-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)


#end
