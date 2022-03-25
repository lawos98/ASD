"""
/=========================================================================================\
|Pokrycie wierzchołkowe                                                                   |
|                                                                                         |
|Mamy dany zbiór zadan T = {t1, . . . , tn}. Kazde zadanie ti                             |
|dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti)     |
|za wykonanie w terminie (liczba naturalna). Wykonanie kazdego zadania trwa jednostke     |
|czasu. Jesli zadanie ti zostanie wykonane przed przekroczeniem swojego terminu d(ti),    |
|to dostajemy za nie nagrode g(ti) (pierwsze wybrane zadanie jest wykonywane w chwili 0,  |
|drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).Prosze podac algorytm,      |
|który znajduje podzbiór zadan, które mozna wykonac w terminie i który prowadzi do        |
|maksymalnego zysku. Prosze uzasadnic poprawnosc algorytmu.                               |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie na posortowaniu całej tablicy   |
|malejąco po profitach a następnie wstawianie pierszym wolnym przed deadline              |
|najbardziej opłacalnych profitów.A następnie po sumowaniu naszych wszystkich profitow    |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Ilość dostępnego czasy             -Maksymalny zysk                                    |
| -Tablica prac                                                                           |
|   -Progit                                                                               |
|   -Deadline                                                                             |
|                                                                                         |
\=========================================================================================/
"""

def maxProfit(P, times):
	P.sort(key=lambda x: x[0],reverse=True)
	T = [-1 for _ in range(times)]
	for profit, deadline in P:
		index = deadline
		while T[index] != -1 and index >= 0:
			index -= 1
		if index != -1:
			T[index] = profit
	res = 0
	for i in T:
		if i != -1:
			res += i

	return res



#end
