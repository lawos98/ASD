"""
/=========================================================================================\
|Rozlokowanie samochodów na prom                                                          |
|                                                                                         |
|Dana jest tablica A[n] z długosciami samochodów, które stoja w kolejce,                  |
|zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba długosci L. Prosze napisac    |
|program, który wyznacza, które samochody powinny pojechac na który pas, zeby na promie   |
|zmiesciło sie jak najwiecej aut.                                                         |
|Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy A.                 |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|czy jest możliwie zmieszczenie i_tych aut przy zachowaniu na jednej plotformie d1 miejsca|
|i przy zachowaniu na drugiej platforie d2 miejsca.Pole jest prawidze jeżeli istnieje     |
|które posiada albo na jednej albo na drugiej platforimie daną długość nowego samochodu   |
|                                                                                         |
|Złożoność czasowa :O(n*L^2)         Złożoność Pamięciowa O(n*L^2)                        |
| Gdzie n to liczba samochodów a L to długość platformy                                   |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica samochodów                 -Dane rozłożenie samochodów                         |
| -długość platofrmy                                                                      |
|                                                                                         |
\=========================================================================================/
"""

def ferry(Tab,L):
	F=[[[False for _ in range(L+1)]for _ in range(L+1)]for _ in range(len(Tab)+1)]
	for i in range(L+1):
		for j in range(L+1):
			F[0][i][j]=True
	for space_1 in range(L,-1,-1):
		for space_2 in range(L,-1,-1):
			for i in range(1,len(Tab)+1):
				if space_1+Tab[i-1]<=L and space_2+Tab[i-1]<=L:
					F[i][space_1][space_2]=F[i-1][space_1+Tab[i-1]][space_2] or F[i-1][space_1][space_2+Tab[i-1]]
				elif space_1+Tab[i-1]<=L:
					F[i][space_1][space_2]=F[i-1][space_1+Tab[i-1]][space_2]
				elif space_2+Tab[i-1]<=L:
					F[i][space_1][space_2]=F[i-1][space_1][space_2+Tab[i-1]]
				else:
					F[i][space_1][space_2]=False
	for space_1 in range(L+1):
		for space_2 in range(L+1):
			if F[len(Tab)][space_1][space_2]==True:
				get_solution(F,len(Tab),space_1,space_2,Tab,L)

def get_solution(Function,i,space_1,space_2,Array,L,Resualt=[]):
	if i==0:
		print(Resualt)
		return
	if space_1+Array[i-1]<=L:
		if Function[i-1][space_1+Array[i-1]][space_2]==True:
			get_solution(Function,i-1,space_1+Array[i-1],space_2,Array,L,Resualt+[[Array[i-1],"L"]])
	if space_2+Array[i-1]<=L:
		if Function[i-1][space_1][space_2+Array[i-1]]==True:
			get_solution(Function,i-1,space_1,space_2+Array[i-1],Array,L,Resualt+[[Array[i-1],"P"]])
	return


#end
