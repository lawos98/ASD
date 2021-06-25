"""
/=========================================================================================\
|Najdłuższy podciąg rosnący                                                               |
|                                                                                         |
|                                                                                         |
|Standardowy problem oparty na programowaniu dynamicznym a mianowicie funkcji która       |
|maksymalną długość ciągu rosnącego kończocego się i-tą wartością                         |
|Aklgorytm zmodyfikowany przy użyciu wyszukiwania binarnego                               |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))       Złożoność Pamięciowa O(n)                           |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Najdłuższe rosnące ciągi                           |
|                                                                                         |
\=========================================================================================/
"""

def binartSearch(Array, left, right, value):
    if left>right:
        return left
    pivot= (left + right) // 2
    if Array[pivot]==value:
        return pivot
    if Array[pivot]>value:
        return binartSearch(Array, left, pivot - 1, value)
    else:
        return binartSearch(Array, pivot + 1, right, value)

def print_lis(A, F, n, m, current):
    if m == 0:
        print(list(reversed(current)))
        return 1
    else:
        count = 0
        for i in range(n):
            if F[i] == m:
                count += print_lis(A, F, i, m - 1, current + [A[i]])
        return count

def lis(A):
    n=len(A)
    Resualt=[]
    F=[0]*n
    for i in range(len(A)):
        index=binartSearch(Resualt,0,len(Resualt)-1,A[i])
        if index==len(Resualt):
            Resualt+=[A[i]]
        else:
            Resualt[index]=A[i]
        F[i]=index+1

    return print_lis(A, F, n, len(Resualt), [])

#end
