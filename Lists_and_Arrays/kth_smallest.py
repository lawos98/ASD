"""
/=========================================================================================\
|Znajdowanie k_tej co do wielkości                                                        |
|                                                                                         |
|Algorytm opiera się na wyszukiwaniu szybkim lecz sortuje tylko tą część tablicy w        |
|której spodziewamy się naszego indeksu                                                   |
|                                                                                         |
|Złożoność czasowa :            Złożoność Pamięciowa O(1)                                 |
| -Optymistyczny:O(n)                                                                     |
| -Pesymistyczny:O(n^2)                                                                   |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""

def partition(Array, left, right):
    x=Array[right]
    i= left - 1
    for j in range(left, right):
        if Array[j]<=x:
            i+=1
            Array[i], Array[j]= Array[j], Array[i]
    Array[i + 1], Array[right]= Array[right], Array[i + 1]
    return i+1

def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return kthSmallest(arr,l,index-1,k)
        return kthSmallest(arr,index+1,r,k -index+l-1)
    return -1
