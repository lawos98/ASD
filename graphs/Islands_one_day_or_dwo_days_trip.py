vfrom queue import PriorityQueue
from math import inf
from math import sqrt
from copy import deepcopy
from random import randint
from collections import deque
#Zad_3
"""
Żeglarz Henryk mieszka na wysepce pewnego archipelagu. Wszystkie wyspy w tym archipelagu są tak małe, że można je
reprezentować jako punkty w przestrzeni R2. Pozycje wszystkich wysp dane są jako ciąg W = ((x1, y1), … , (xn, yn)).
Henryk mieszka na wyspie(x1, y1), ale chce się przeprowadzić na wyspę (xn, yn).  Normalnie, każdego dnia może
przepłynąć na wyspę znajdującą się w odległości najwyżej Z (w sensie standardowej odległości euklidesowej),
ale może także każdego dnia przepłynąć odległość do 2Z, pod warunkiem, że cały następny dzień będzie odpoczywał.
Henryk musi zawsze nocować na jakiejś wyspie. Proszę zaproponować (bez implementacji) wielomianowy algorytm, który
oblicza ile minimalnie dni Henryk potrzebuje, żeby dostać się na swoją docelową wyspę (lub stwierdza, że to niemożliwe).
"""

def fast_way(Table,start,end,z):

	def odl(point_a,point_b):
		return sqrt(((point_a[0]-point_b[0])**2)+((point_a[1]-point_b[1])**2))

	def make_graph(D1,Table,z):
		n=len(Table)
		for i in range(n-1):
			for j in range(i+1,n):
				if odl(Table[i],Table[j])<=z:
					D1[i]+=[j]
					D1[j]+=[i]
				elif odl(Table[i],Table[j])<=2*z:
					D1+=[[i,j]]
					D1[i]+=[len(D1)-1]
					D1[j]+=[len(D1)-1]

	Graph=[[]for _ in range(len(Table))]
	print(len(Table))
	make_graph(Graph,Table,z)
	for i  in range(len(Graph)):
		print(i,"|",Graph[i])
	q=deque()
	visited = [False]*len(Graph)
	distant=[-1]*len(Graph)
	distance=0

	q.append(start)
	visited[start] = True
	distant[start]=0

	while len(q)!=0:
		distance+=1
		for _ in range(len(q)):
			u = q.pop()
			for v in Graph[u]:
				if not visited[v]:
					visited[v] = True
					distant[v]=distance
					q.append(v)
	print(distant[end])


T=[]
for i in range(20):
	T+=[[randint(1,100),randint(1,100)]]
print(T)
fast_way(T,5,10,10)
