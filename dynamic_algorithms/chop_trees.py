"""
/=========================================================================================\
|Ścinanie drzew                                                                           |
|                                                                                         |
|                                                                                         |
|Black Forest to las rosnacy na osi liczbowej gdzies w południowej Anglii. Las            |
|składa sie z n drzew rosnacych na pozycjach 0, . . . ,n−1. Dla kazdego i >               |
|{0, . . . ,n−1} znany jest zysk ci, jaki mozna osiagnac scinajac drzewo z pozycji i.     |
|John Lovenoses chce uzyskac maksymalny zysk ze scinanych drzew, ale prawo zabrania       |
|scinania dwóch drzew pod rzad. Prosze zaproponowac algorytm, dzieki któremu              |
|John znajdzie optymalny plan wycinki.                                                    |
|                                                                                         |
|Algorytm opiera się na programowaniu dynaminicznym a mianowice na funckji zwracającej    |
|maksymalny zysk  po ścieciu drzew przy zachowaniu warunku aby nie ścinać obok siebie     |
|dwóch drzew do i-tego drzewa.Fukcja dla itego pola wylicza maksimum z fukcji o jedno     |
|drzewo mniej lub dwa drzewa mniej wraz z naszym obecnym i-tym drzewem                    |
|                                                                                         |
|Złożoność czasowa :O(n)              Złożoność Pamięciowa O(n)                           |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Najwiekszy zysk po ścieciu drzew                   |
|                                                                                         |
\=========================================================================================/
"""

def chop_trees(Array):
    n=len(Array)
    F=[0 for _ in range(n+1)]
    F[1]=Array[0]
    for i in range(2,n+1):
        F[i]=max(F[i-1],F[i-2]+Array[i-1])
    return F[n]


#end
