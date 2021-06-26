"""
/=========================================================================================\
|Ładowanie przyczepy wartościami bitowymi                                                 |
|                                                                                         |
|Mamy przyczepe o pojemnosci K kilogramów oraz zbiór ładunków                             |
|o wagach w1, . . . ,wn. Waga kazdego z ładunków jest potega dwójki                       |
|(czyli, na przykład, dla siedmiu ładunków wagi moga wynosic 2, 2, 4, 8, 1, 8, 16,        |
|a pojemnosc przyczepy K = 27). Prosze podac algorytm zachłanny (i uzasadnic jego         |
|poprawnosc), który wybiera ładunki tak, ze przyczepa jest mozliwie maksymalnie zapełniona|
|(ale bez przekraczania pojemnosci) i jednoczesnie uzylismy mozliwie jak najmniej         |
|ładunków. (Ale jesli da sie np. załadowac przyczepe do pełna uzywajac 100 ładunków,      |
|albo zaladowac do pojemnosci K − 1 uzywajac jednego ładunku, to lepsze                   |
|jest to pierwsze rozwiazanie).                                                           |
|                                                                                         |
|Algorytm opiera się na algorytmie zachłanym a mianowicie na posortowaniu całej tablicy   |
|malejąco a następnie dołaczaniu wartości ktore mieszczą się na cieżarówce                |
|                                                                                         |
|Złożoność czasowa :O(n)             Złożoność Pamięciowa O(n)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica wag                        -Tablica załadunku                                  |
| -Maksymalna ładowność                                                                   |
|                                                                                         |
\=========================================================================================/
"""

def bit_truck(Array,K):
	Array.sort(reverse=True)
	index=0
	Result=[]
	while index!=len(Array)-1:
		if Array[index]<=K:
			K-=Array[index]
			Result+=[Array[index]]
		index+=1
	return Result


#end
