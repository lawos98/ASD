from queue import PriorityQueue
from math import inf
from math import sqrt
from copy import deepcopy
from random import randint
from collections import deque
#Zad_4
"""
Sasza kolekcjonuje rosyjskie lalki - matrioszki. Każda z nich ma określoną wysokość X i szerokość Y,
dane liczbami naturalnymi dodatnimi. Jedną matrioszkę można włożyć do drugiej, jeżeli ma od niej
mniejszą zarówno wysokość, jak i szerokość.
Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei.
Pomóż mu znaleźć odpowiedź na to pytanie.
"""

def Matriosha(Array):
	Array.sort()
	print(Array)

	def binartSearch(Array, left, right, value):
		if abs(left-right)==1 or left==right:
			if right<value:
				return right
			else:
				return left
		pivot= (left + right) // 2
		if Array[pivot]<value:
			return binartSearch(Array,pivot,right,value)
		else:
			return binartSearch(Array,left,pivot-1,value)

	Base=[Array[0][1]]
	for i in range(len(Array)):
		current=Array[i][1]
		print(Base,current)
		index=binartSearch(Base,0,len(Base)-1,current)
		if current>Base[index]:
			if index==len(Base)-1:
				Base+=[current]
			elif Base[index+1]>current:
				Base[index+1]=current
	print(Base)




Tab=[[2,2],[3,12],[5,20],[6,11],[11,18],[10,20],[6,16],[8,20],[15,15],[17,25],[30,30]]
Matriosha(Tab)
