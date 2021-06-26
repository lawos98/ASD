"""
/=========================================================================================\
|Złe dziecko kradnie klocki                                                               |
|                                                                                         |
|Grupa m dzieci bawi sie w układanie mozliwie jak najwiekszej wiezy. Kazde dziecko        |
|ma klocki róznej wysokosci. Pierwsze dziecko ma klocki o wysokosciach w1,w2,...,drugie   |
|dziecko klocki o wyskościach w1,w2,.... itd.Dzieci własnie poszły zjesc deser            |
|zanim ułoza swoje wieze, ale jedno dziecko zostało. Ma teraz jedyna okazje, zeby         |
|podebrac kilka klocków innym dzieciom tak, zeby jego wieza była najwyzsza.               |
|Prosze podac mozliwie najszybszy algorytm rozwiazujacy ten problem, który zabiera        |
|minimalna ilosc klocków. (Prosze zwrócic uwage, ze liczby w-i moga byc bardzo duze.)     |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie złe dziecko kradnie maksymalny  |
|zysk wysokości w porównaniu z maksymalną aktualną wysokością z wszystkich                |
|wieży po koleji                                                                          |
|                                                                                         |
|Złożoność czasowa :O(k*n)             Złożoność Pamięciowa O(n)                          |
| -Gdzie n to liczba wież a k to liczba klocków                                           |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica wież z klockami            -Aktualne ruchy złego dziecka                       |
| -(wieża 0 jest złego dziecka)                                                           |
|                                                                                         |
\=========================================================================================/
"""
def steal(towers):
    towers = [sorted(t, reverse=True) for t in towers]
    Towers_height = [sum(t) for t in towers]

    max_height = max(Towers_height)
    my_height = Towers_height[0]

    delta = max_height - my_height

    while delta >= 0:
        best_tower = None
        best_delta = delta
        for tower_i in range(1, len(towers)):
            if len(towers[tower_i]) == 0:
                continue

            Towers_height[tower_i] -= towers[tower_i][0]
            my_height += towers[tower_i][0]

            new_winning_height = max(Towers_height[1:])
            new_delta = new_winning_height - my_height

            if new_delta < best_delta:
                best_tower = tower_i
                best_delta = new_delta

            my_height -= towers[tower_i][0]
            Towers_height[tower_i] += towers[tower_i][0]

        print("Stole block", towers[best_tower][0], "from tower", best_tower)
        Towers_height[best_tower] -= towers[best_tower][0]
        my_height += towers[best_tower][0]
        towers[best_tower].pop(0)
        delta = best_delta


#end
