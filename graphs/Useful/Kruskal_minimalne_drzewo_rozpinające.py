"""
1.Posortuj krawędzie po wagach
2.Utwórz pusty zbiór A
3.Przegladaj krawedzie w kolejności niemalejących wag
-jesli nie zawiera cyklu to dołacz do A
4.Zwróć A
złożoność Elog(V)
"""



class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self
        self.rank=0

def find(x):
    if x!=x.parent:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def kruskal(Array):
    n=len(Array)
    Array.sort(key=lambda x: x[2])
    V=[Node(i) for i in range(n)]
    Resualt=[]
    for i in Array:
        if find(V[i[0]])!=find(V[i[1]]):
            union(V[i[0]],V[i[1]])
            Resualt+=[[i[0],i[1]]]
    print(Resualt)

Tab=[[0,1,1],[0,2,8],[1,0,1],[1,2,7],[1,3,3],[2,0,8],[2,1,7],[2,4,12],
     [2,5,2],[3,1,3],[3,4,7],[4,2,12],[4,3,7],[4,5,4],[5,2,2],[5,4,4],
     [5,6,10],[5,7,6],[6,5,10],[6,7,5],[7,5,6],[7,6,5]]

kruskal(Tab)
