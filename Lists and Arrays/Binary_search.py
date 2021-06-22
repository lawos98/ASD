"""
/=========================================================================================\
|Wyszukiwanie binarne                                                                     |
|                                                                                         |
|algorytm opierający się na metodzie dziel i zwyciężaj, który w czasie logarytmicznym     |
|twierdza, czy szukany element znajduje się w uporządkowanej tablicy i jeśli się          |
|znajduje, podaje jego indeks.                                                            |
|                                                                                         |
|Złożoność czasowa :O(log(n))             Złożoność Pamięciowa O(1)                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -indeks pierwszego elementu w Tablicy               |
| -Początek Tablicy                                                                       |
| -Koniec Tablicy                                                                         |
| -Szukana wartość                                                                        |
|                                                                                         |
\=========================================================================================/
"""

def binartSearch(Array, left, right, value):
    if left>right:
        return None
    pivot= (left + right) // 2
    if Array[pivot]==value:
        current=binartSearch(Array, left, pivot - 1, value)
        if current==None:return pivot
        return current
    if Array[pivot]>value:
        return binartSearch(Array, left, pivot - 1, value)
    else:
        return binartSearch(Array, pivot + 1, right, value)
