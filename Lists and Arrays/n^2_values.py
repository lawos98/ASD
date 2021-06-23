"""
/=========================================================================================\
|Sortowanie wartości do n^2                                                               |
|                                                                                         |
|Prosze zaproponowac algorytm, który w czasie liniowym sortuje tablice A zawierajaca      |
|n liczb ze zbioru 0, . . . ,n^2 − 1.                                                     |
|                                                                                         |
|Algorytm opiera się na sortowaniu pozycyjnym począwszy od reszcie z dzielenia przez n    |
|a następnie po dzieleniu całkowitym przez n
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(n)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""

def countSort(arr, n, exp):
    output = [0] * n
    count = [0] * n
    for i in range(n):
        count[ (arr[i] // exp) % n ] += 1
    for i in range(1, n):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[ (arr[i] // exp) % n] - 1] = arr[i]
        count[(arr[i] // exp) % n] -= 1
    for i in range(n):
        arr[i] = output[i]
def sort(arr) :
    n=len(arr)
    countSort(arr, n, 1)
    countSort(arr, n, n)


#end
