"""
/=========================================================================================\
|Algorytm sortowania szybkiego                                                            |
|                                                                                         |
|Polega na wybraniu elementu rozdzielającego,a następnie tablica jest dzielona na dwa     |
|fragmenty do początkowego przenoszone są wszystkie elementy nie większe od               |
|rozdzielającego, do końcowego wszystkie większe.Potem sortuje się osobno początkową      |
|i końcową część tablicy.Rekursja kończy się, gdy kolejny fragment uzyskany z podziału    |
|zawiera pojedynczy element, jako że jednoelementowa tablica nie wymaga sortowania.       |
|pozostał już tylko jeden element.Następnie połaczenie posortowanych ciągów               |
|                                                                                         |
|Złożoność czasowa :O(n*log(n))           Złożoność Pamięciowa O(log(n))(Tail Call)       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Początek listy odsyłaczowej        -Początek listy odsyłaczowej                        |
|                                                                                         |
\=========================================================================================/
"""

def quicksort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p<r-q:
            quicksort(A,p,q-1)
            p=q+1
        else:
            quicksort(A,q+1,r)
            r=q-1


def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


#end
