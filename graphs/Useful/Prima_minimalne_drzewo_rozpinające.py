from math import inf
from queue import PriorityQueue

def prim(Array,s):
    n=len(Array)
    d=[inf]*n
    parent=[-1]*n
    d[s]=0
    Q=PriorityQueue()
    Q.put([d[s],s])
    while not Q.empty():
        u=Q.get()
        u=u[1]
        for v,w in Array[u]:
            if w<d[v]:
                d[v]=w
                Q.put([d[v],v])
                parent[v]=u

    print(parent)

Tab=[[0,1,1],[0,2,8],[1,0,1],[1,2,7],[1,3,3],[2,0,8],[2,1,7],[2,4,12],
     [2,5,2],[3,1,3],[3,4,7],[4,2,12],[4,3,7],[4,5,4],[5,2,2],[5,4,4],
     [5,6,10],[5,7,6],[6,5,10],[6,7,5],[7,5,6],[7,6,5]]

Tab2=[[[1,1],[2,8]],
      [[0,1],[2,7],[3,3]],
      [[0,8],[1,7],[4,12],[5,2]],
      [[1,3],[4,7]],
      [[2,12],[3,7],[5,4]],
      [[2,1],[4,6],[6,10],[7,6]],
      [[5,10],[7,5]],
      [[5,6],[6,5]]]

prim(Tab2,0)
