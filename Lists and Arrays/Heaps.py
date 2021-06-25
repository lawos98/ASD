#heapify O(logN)
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

#delete O(Logn)
def deleteroot(A,n):
    last=A[n-1]
    A[0]=last
    A.pop(n-1)
    heapify(A,n-1,0)

#build O(N) liscie mozna pominac ze wzgeldu na brak dzialania heapify
def buildheap(A):
    n=len(A)
    for i in range(n,-1,-1):
        heapify(A,(n//2)-1,i)

def heapify_parent(A,n,i):
    parent=(i-1)//2
    if parent>=0:
        if A[i]>A[parent]:
            A[i],A[parent]=A[parent],A[i]
            heapify_parent(A,n,parent)

#insert O(Logn)
def insert(A,n,value):
    n=n+1
    A+=[value]
    heapify_parent(A,n,n-1)

#heapsort O(nLogn)
def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)

#convert Min_heap to Max_heap O(N) (może sie wydawać zę jest O(NlogN)
def convert_to_MaxHeap(arr, n):
    for i in range((n-2)//2,-1,-1):
        heapify(arr, n,i)

# Merges Max heaps a[] and b[] into merged[]
def mergeHeaps(merged, a, b, n, m):
    for i in range(n):
        merged[i] = a[i]
    for i in range(m):
        merged[n + i] = b[i]
    buildHeap(merged, n + m)


#end
