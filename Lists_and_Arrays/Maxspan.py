"""
/=========================================================================================\
|Największa odległośc w posortowanej liscie dwóch kolejnych elementów                     |
|                                                                                         |
|Dana jest tablica A zawierajaca n parami róznych liczb. Prosze zaproponowac              |
|algorytm, który znajduje takie dwie liczby x i y z A, ze y −x jest jak najwieksza oraz   |
|w tablicy nie ma zadnej liczby z takiej, ze x < y < z (innymi słowy, po posortowaniu     |
|tablicy A rosnaco wynikiem byłyby liczby A[i] oraz A[i+1] dla których A[i + 1] − A[i]    |
|jest najwieksze).                                                                        |
|                                                                                         |
|Algorytm opiera się na sortowaniu kubełkowym który oblicza odległości miedzy kolejnymi   |
|kubełkami,następnie zwraca maksymalną wartość                                            |
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(n)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Szukana wartość                                    |
|                                                                                         |
\=========================================================================================/
"""

def maxspan(A):
    n = len(A)
    minimum = A[0]
    maximum = A[0]
    for i in range(n):
        minimum = min( minimum, A[i])
        maximum = max( maximum, A[i])

    B=[[] for _ in range(n)]
    x = (maximum + minimum) / n

    for i in range(n):
        d=int((A[i] - minimum)/x)
        B[d]+=[A[i]]

    result = 0
    prev_max = max(B[0])
    for i in range(1,n):
        if len(B[i]) != 0:
            act_min  = min( B[i])
            result   = max( result, act_min - prev_max )
            prev_max = max( B[i])

    return result


#end
