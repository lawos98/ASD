"""
/=========================================================================================\
|Wydawanie monet                                                                          |
|                                                                                         |
|Mamy dana tablice z nominałami monet stosowanych w pewnym dziwnym                        |
|kraju, oraz kwote T. Prosze podac algorytm, który oblicza minimalna ilosc monet potrzebna|
|do wydania kwoty T (algorytm zachłanny, wydajacy najpierw najwieksza monete, nie działa: |
|dla monet 1, 5, 8 wyda kwote 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).                   |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|minimalną liczbę monet aby osignąć i-tą wartość.Wyliczana jest on jako minmalna wartość  |
|z wartości mniejszych od niej o watrtość monety oraz plus 1                              |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica Monet                      -Minimalna liczba monet                             |
| -szukana wartość                                                                        |
|                                                                                         |
\=========================================================================================/
"""
def coins2( x, M ):
    T=[x+1 for _ in range(x+1)]
    T[0] = 0
    for y in range(x+1):
        for m in M:
            if y >= m:
               T[y] = min(T[y],T[y-m]+1)
    print(T)
    return T[x]
