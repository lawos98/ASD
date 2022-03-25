"""
/=========================================================================================\
|Skacząca żaba                                                                            |
|                                                                                         |
|Prosze zaproponowac algorytm dla dwuwymiarowej                                           |
|wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn}            |
|przedmiotów i dla kazdego przedmiotu pi dane sa nastepujace trzy liczby:                 |
|v(pi) – wartosc przedmiotu,  w(pi) – waga przedmiotu, oraz ,h(pi) – wysokosc przedmiotu. |
|Złodziej chce wybrac przedmioty o maksymalnej wartosci, których łaczna waga nie          |
|przekracza danej liczby W oraz których łaczna wysokosc nie przekracza danej liczby       |
|H (przedmioty zapakowane sa w kartony, które złodziej układa jeden na drugim).           |
|Prosze oszacowac złozonosc czasowa swojego algorytmu oraz uzasadnic jego poprawnosc.     |
|                                                                                         |
|Standardowy problem plecakowy rozważany z dwoma warunkami.Przez co dokładamy do naszej   |
|funkcji dodatkowy wymiar i rozpatrzamy analogicznie.                                     |
|                                                                                         |
|Złożoność czasowa :O(n*Max_W*Max_H) Złożoność Pamięciowa O(n*Max_W*Max_H)                |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Maksymalna dopuszczalna waga         -maksymalny profit pod warunkami                  |
| -Tablica wag                                                                            |
| -Tablica profitow                                                                       |
| -Tablica wysokości                                                                      |
| -Maksymalna wysokość                                                                    |
|                                                                                         |
\=========================================================================================/
"""

def knapSack(Max_W, Weight, Profit, Height, Max_H):
	lenght=len(Profit)
	F = [[[0 for x in range(Max_W + 1)] for _ in range(Max_H + 1)] for x in range(lenght + 1)]
	for i in range(lenght + 1):
		for h in range(Max_H + 1):
			for w in range(Max_W + 1):
				if 0<=h-Height[i - 1]<=Max_H and 0<=w - Weight[i - 1]<=Max_W:
					F[i][h][w] =max(Profit[i - 1] + F[i - 1][h - Height[i - 1]][w - Weight[i - 1]], F[i - 1][h][w])
				else:
					F[i][h][w] = F[i - 1][h][w]
	return F[lenght][Max_H][Max_W]


#end
