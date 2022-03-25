"""
/=========================================================================================\
|Inny problem plecakowy                                                                   |
|                                                                                         |
|Prosze podac i zaimplementowac algorytm znajdujacy wartosc optymalnego                   |
|zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działac w czasie |
|wielomianowym wzgledem liczby przedmiotów oraz sumy ich profitów.                        |
|                                                                                         |
|Standardowy problem pleckakowy ze zmianą fukcji na i_ty przedmiot oraz j-profit który    |
|minimalną wagę potrzebną do wyżej wymienionego profitu                                   |
|                                                                                         |
|Złożoność czasowa :O(max_p*w)       Złożoność Pamięciowa O(max_p*w)                      |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica wag                        -Optymalny zbiór przedmiotów                        |
| -Tablica profitów                                                                       |
| -maksymalna dopuszczalna waga                                                           |
|                                                                                         |
\=========================================================================================/
"""

def knapsack(W, P, max_w):
    if max_w == 0:
        return []

    n = len(W)
    max_p = sum(P)

    F = [[-1] * (max_p + 1) for _ in range(n)]

    for p in range(max_p + 1):
        if W[0] <= max_w and P[0] >= p:
            F[0][p] = W[0]

    for i in range(n):
        F[i][0] = 0

    for i in range(1, n):
        for p in range(1, max_p + 1):
            F[i][p] = max_w + 1

            if F[i - 1][p] > -1:
                F[i][p] = min(F[i][p], F[i - 1][p])

            if F[i - 1][p - P[i]] > -1:
                F[i][p] = min(F[i][p], F[i - 1][p - P[i]] + W[i])

            if F[i][p] == max_w + 1:
                F[i][p] = -1

    best_p = 0
    for p in range(0, max_p + 1):
        if -1 < F[n - 1][p] <= max_w and p > best_p:
            best_p = p

    return best_p, F


def get_solution(F, W, P, i, w, p):
    if i == 0:
        return [0] if W[0] <= w else []

    if W[i] <= w and F[i - 1][p - P[i]] == F[i][p] - W[i]:
        return get_solution(F, W, P, i - 1, w - W[i], p - P[i]) + [i]
    else:
        return get_solution(F, W, P, i - 1, w, p)


#end
