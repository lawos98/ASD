"""
/=========================================================================================\
|Suma podzbioru                                                                           |
|                                                                                         |
|Dana jest tablica n liczb naturalnych A. Prosze podac i zaimplementowac                  |
|algorytm, który sprawdza, czy da sie wybrac podciag liczb z A, które sumuja sie do       |
|zadanej wartosci T.                                                                      |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|czy jest mozliwość utoworzenia sumy równej j do i-tego elementu.Zwracana wartość pola    |
|zależy od alternatywy wyrażenie funkcji zawierającą jedną wartość i mniej oraz wyrażenia |
|funkcji zawierającą jedną i-tą wartość mniej oraz sumy zmniejszonej o i_tą wartość       |
|z wartości mniejszych od niej o watrtość monety oraz plus 1                              |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(n^2)                          |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -True/False                                         |
| -szukana suma                                                                           |
|                                                                                         |
\=========================================================================================/
"""

def subsetsum(Array, t):
    n=len(Array)

    F=([[False for i in range(t+1)] for i in range(n+1)])

    for i in range(n+1):
        F[i][0]=True

    for i in range(1,n+1):
        for j in range(1,t+1):
            if j<Array[i - 1]:
                F[i][j]=F[i-1][j]
            if j>= Array[i - 1]:
                F[i][j]=F[i-1][j] or F[i-1][j - Array[i - 1]]

    return F[n][t]


#end
