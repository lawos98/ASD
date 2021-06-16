"""
/=========================================================================================\
|Algorytm sortowania przez zliczanie                                                      |
|                                                                                         |
|Na początku działania algorytmu ustalany jest przedział wartości, które zależą od        |
|wartości wszystkich elementów w sekwencji, która ma być posortowana                      |
|Dla każdego elementu z utworzonego przedziału obliczana jest ilość jego wystąpień        |
|w wejściowej sekwencji.Następny krok polega na analizie wszystkich elementów listy       |
|zliczającej. i-tą liczbę na liście wypisujemy tyle razy jaką wartość ma lista pod        |
|indeksem i. W ten sposób uzyskujemy posortowaną listę. Jeśli listę zliczającą            |
|będziemy przeglądać od lewej do prawej to uzyskamy listę posortowaną rosnącą.            |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""


def counting_sort(Array, min, max):
    lenght = max - min + 1
    Array_count=[0] * lenght

    for number in Array:
        Array_count[number - min] += 1

    for i in range(1, lenght):
        Array_count[i] += Array_count[i - 1]

    Resualt=[0]*len(Array)
    for number in range(len(Array)-1,-1,-1):
        index=Array[number]-min
        Array_count[index] -= 1
        Resualt[Array_count[index]] = Array[number]

    return Resualt
