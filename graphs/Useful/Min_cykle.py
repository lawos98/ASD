def min_cycle( G ):

    def find_min_vertex(Distance,Visited,n):
        vertex=-1
        min_vertex=inf
        for i in range(n):
            if Visited[i]==False and 0<Distance[i]<min_vertex:
                vertex=i
                min_vertex=Distance[i]
        return vertex

    def Dikstry(Graph, s):
        n=len(Graph)
        d=[inf]*n
        parent=[-1]*n
        visited=[False]*n
        d[s]=0
        u=s
        while u!=-1:
            visited[u]=True
            for i in range(len(Graph)):
                if Graph[u][i]>0 and d[u]+Graph[u][i]<d[i]:
                    d[i]=d[u]+Graph[u][i]
                    parent[i]=u
            u=find_min_vertex(d,visited,n)
        return parent

    def short_distant(Array,x,y):
        Path=Dikstry(Array,x)
        distant=0
        point_b=y
        point_a=Path[y]
        Resualt=[y]
        while point_a!=-1:
            Resualt+=[point_a]
            distant+=Array[point_a][point_b]
            point_b=point_a
            point_a=Path[point_a]
        return distant,Resualt

    n=len(G)
    min_cykle_len=inf
    min_cykle_path=[]
    for i in range(n):
        for j in range(i+1,n):
            if G[i][j]>0:
                G[i][j]=-G[i][j]
                G[j][i]=-G[j][i]
                cykle=short_distant(G,i,j)
                G[i][j]=-G[i][j]
                G[j][i]=-G[j][i]
                cykle_len=cykle[0]+G[j][i]
                cykle_path=cykle[1]
                if cykle_len<min_cykle_len and cykle[0]>0:
                    min_cykle_len=cykle_len
                    min_cykle_path=cykle_path
    return min_cykle_path
