"""
/=========================================================================================\
|Sprawiedliwy podział pracy                                                               |
|                                                                                         |
|Prosze podac i zaimplementowac algorytm znajdujacy wartosc optymalnego                   |
|zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działac w czasie |
|wielomianowym wzgledem liczby przedmiotów oraz sumy ich profitów.                        |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|minimalną liczbę pracy tak aby każdy z pracowników pracował możliwie jak najmniej        |
|ktora zależy od dwóch argumentów liczy elementów do wykonania pracy oraz liczby          |
|pracownikow.Wyliczana jest on z podziału pracy na funkcje do danego przeciecia łacznej   |
|pracy oraz reszty pracy po przecieciu dla nowej osoby                                    |
|                                                                                         |
|Złożoność czasowa :O(n*t)       Złożoność Pamięciowa O(n*t)                              |
| Gdzie n to liczba pracy a t to liczba pracowników                                       |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica pracy                      -Minimalna praca w sprawiedliwym podziale           |
| -liczba pracowników                                                                     |
|                                                                                         |
\=========================================================================================/
"""
from math import inf
def distribution_work(Array,workers):
    n=len(Array)
    F=[[-inf for _ in range(workers+1)] for _ in range(n+1)]
    for i in range(n+1):
        F[i][1]=sum(Array[:i])
    for t in range(2,workers+1):
        for i in range(n+1):
            for o in range(i+1):
                F[i][t]=max(F[i][t],min(F[i-o][t-1],sum(Array[i-o:i])))
    return F[n][workers]


#end
