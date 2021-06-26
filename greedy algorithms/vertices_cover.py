"""
/=========================================================================================\
|Pokrycie wierzchołkowe                                                                   |
|                                                                                         |
|Dany jest zbiór punktów X = {x1, . . . , xn} na                                          |
|prostej. Prosze podac algorytm, który znajduje minimalna liczbe przedziałów              |
|jednostkowych domknietych, potrzebnych do pokrycia wszystkich punktów z X.               |
|(Przykład: Jesli X = {0.25, 0.5, 1.6} to potrzeba dwóch przedziałów,                     |
|np. [0.2, 1.2] oraz [1.4, 2.4]).                                                         |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie na posortowaniu całej tablicy   |
|a następnie rozpoczęciu przedziału i zwiekszeniu indeksu jeżeli następne punkty należą   |
|do przedziału.Jeżeli nie należy rozpoczynamy nowy przedział                              |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica punktów                    -Tablica z minimalna liczba odcinków                |
|                                                                                         |
\=========================================================================================/
"""

def vertices_cover(T):
  n = len(T)
  Result = []
  T.sort()

  i = 0
  while i < n:
    start = T[i]
    i += 1
    stop = start+1

    while i < n and T[i] <= stop:
      i += 1

    Result+=[[start,stop]]

  return Resualt


#end
