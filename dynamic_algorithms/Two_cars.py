from queue import PriorityQueue
from math import inf
from math import sqrt
from copy import deepcopy
from random import randint
from collections import deque
#Zad_4
"""
Wyjeżdżacie ze znajomymi na wakacje. Macie dwa samochody i N bagaży o łącznej wadze W. Waga każdego z bagaży jest
liczbą naturalną dodatnią. Czy jesteście w stanie tak je zapakować, aby w obu samochodach były bagaże o tej samej
łącznej wadze?
"""


def car(W):
	n=len(W)
	sum=0
	for i in range(n):
		sum+=W[i]
	if sum%2!=0:
		print("1.Nie",sum)
	else:
		wmax=sum//2
		Tab=[[0 for _ in range(wmax+1)]for _ in range(n+1)]
		for i in range(n+1):
			Tab[i][0]=1
		for i in range(1,n+1):
			for w in range(1,wmax+1):
				if w-W[i-1]>=0:
					Tab[i][w]=max(Tab[i-1][w],Tab[i-1][w-W[i-1]])
		for i in range(n+1):
			for w in range(wmax+1):
				print(Tab[i][w],end=" , ")
			print()
		print(Tab[n-1][wmax])


Tab=[5,3,10]
car(Tab)
