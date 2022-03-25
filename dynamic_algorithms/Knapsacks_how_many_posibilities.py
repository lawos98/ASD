from queue import PriorityQueue
from math import inf
from copy import deepcopy
from random import randint


#zad.2
"""
Złodziej włamuje się do sklepu z przedmiotami o wagach i cenach, będących liczbami naturalnymi dodatnimi. Chowa je
do plecaka, w którym może unieść rzeczy o łącznej maksymalnej wadze Wmax. Tak, tak, znamy tę historię. Ale tym razem
złodziejowi nie zależy na tym, by ukraść artykuły o najwyższej możliwej łącznej cenie. Interesuje go za to, na ile
sposobów może wybrać przedmioty, aby ich łączna cena była równa co najmniej Cmin oraz aby ich łączna waga
nie przekraczała Wmax.
"""

def knapsack_pos(W,C,Wmax,Cmin):
	n=len(W)+1
	Tab=[[[0 for _ in range(Cmin+1)]for _ in range(Wmax+1)]for _ in range(n)]
	for i in range(n):
		Tab[i][0][0]=1
	for j in range(Wmax+1):
		Tab[0][j][0]=1
	for i in range(1,n):
		for w in range(1,Wmax+1):
			for c in range(Cmin+1):
				if w-W[i-1]>0:
					Tab[i][w][c]=Tab[i-1][w-W[i-1]][max(c-C[i-1],0)]+Tab[i-1][w][c]
	print(Tab[n-1][Wmax][Cmin])




W=[1,2,3,4]
C=[1,6,4,9]

knapsack_pos(W,C,50,10)
