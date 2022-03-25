"""
/=========================================================================================\
|Skacząca żaba                                                                            |
|                                                                                         |
|Pewna zaba skacze po osi liczbowej. Ma sie dostac z zera do n − 1, skaczac               |
|wyłacznie w kierunku wiekszych liczb. Skok z liczby i do liczby j (j > i) kosztuje       |
|ja j − i jednostek energii, a jej energia nigdy nie moze spasc ponizej zera.             |
|Na poczatku zaba ma 0 jednostek energii, ale na szczescie na niektórych liczbach—takze   |
|na zerze—leza przekaski o okreslonej wartosci energetycznej (wartosc przekaki            |
|dodaje sie do aktualnej energii Zbigniewa). Prosze zaproponowac algorytm,                |
|który oblicza minimalna liczbe skoków potrzebna na dotarcie z 0 do n − 1 majac           |
|dana tablice A z wartosciami energetycznymi przekasek na kazdej z liczb.                 |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|minimalną wartość skoków aby dotrzeć do i-tego pola wraz z daną energią                  |
|jest to możliwe wtedy i tylko wtedy jeżeli do pola oddalonego o długość skoku ("jump")   |
|oraz wartość energetyczną owego skoku wraz z uwzglednieniem otrzymanego na danym polu    |
|energi                                                                                   |
|                                                                                         |
|Złożoność czasowa :O(n^2*max_energy)         Złożoność Pamięciowa O(n^2*max_energy)      |
| Gdzie n to liczba pól a max_energy to maksymalna energia jaką można osiągnąć            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica pól wraz z energią         -minimalna ściezka po której porusa się żaba        |
|                                                                                         |
\=========================================================================================/
"""


from math import inf
def frog(Array):
	n=len(Array)
	max_energy=sum(Array)
	F=[[inf for _ in range(max_energy+1)]for _ in range(n)]
	Parent=[-1]*n
	K=[inf]*n
	F[0][Array[0]]=0
	for i in range(1,n):
		for energy in range(max_energy+1):
			for jump in range(1,i+1):
				if 0<=energy+jump-Array[i]<=max_energy:
					if energy-Array[i]>0:
						F[i][energy]=min(F[i][energy],F[i-jump][energy+jump-Array[i]]+1)
						if K[i]>F[i][energy]:
							Parent[i]=i-jump
							K[i]=F[i][energy]
	Resualt=[n-1]
	n=n-1
	while Parent[n]!=-1:
		n=Parent[n]
		Resualt=[n]+Resualt
	return Resualt
