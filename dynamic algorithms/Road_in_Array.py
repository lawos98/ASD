"""
/=========================================================================================\
|Wędrówka po szachownicy                                                                  |
|                                                                                         |
|Dana jest szachownica A o wymiarach n × n. Szachownica                                   |
|zawiera liczby wymierne. Nalezy przejsc z pola (1, 1) na pole (n,n) korzystajac          |
|jedynie z ruchów “w dół” oraz “w prawo”. Wejscie na dane pole kosztuje tyle, co          |
|znajdujaca sie tam liczba. Prosze podac algorytm znajdujacy trase o minimalnym koszcie.  |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|minimalną odległość od punktu 0,0 do i,j .Fukcja opiera się na wybieraniu minimalnej     |
|wartości z lewego jak i górnego pola                                                     |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(n^2)                          |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablice                            -Optymalna wartość drogi                            |
|                                                                                         |
\=========================================================================================/
"""

def mincost(Array):
    m = len(Array)
    n = len(Array[0])
    Costs = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            Costs[i][j] = Array[i][j]

            if i ==0 and j>0:
                Costs[0][j]+=Costs[0][j-1]

            elif j==0 and i>0:
                Costs[i][0] += Costs[i-1][0]

            elif i>0 and j >0:

                Costs[i][j]+=min(Costs[i-1][j], Costs[i][j-1])

    return Costs[m-1][n-1]


#end
