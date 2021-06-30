def euler( G ):


    #sprawdzenie warunku spójności grafu
    def dfs_check(graph, s):
        visited = [False]*len(graph)
        number=len(graph)-1
        def dfs_visit(u):
            nonlocal graph,visited,number
            visited[u]=True
            for v in range(len(graph)):
                if not visited[v] and graph[min(u,v)][max(u,v)]:
                    number-=1
                    dfs_visit(v)
        if number==0:
            return False
        return True

    #sprawdzenie parzystości wierzchołkowej
    def odd_check(deg):
        for i in range(len(deg)):
            if deg[i]%2==1:
                return True
        return False

    #Tworzenie tablic stopni wierzchołków,Macierzy krawędzi
    degree=[0 for _ in range(len(G))]
    matrix=[[None for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j]=G[i][j]
            if matrix[i][j]==1:
                degree[i]+=1
                degree[j]+=1

    #Sprawdzenie warunków koniecznych
    if dfs_check(matrix,0) and odd_check(degree):
        return None

    #Algorytm znajdowania Cyklu Eulera
    def dfs(graph,deg,s):
        q=[]
        def dfs_visit(u):
            nonlocal graph,deg,q
            for v in range(len(graph)):
                if graph[min(u,v)][max(u,v)]==1:
                    graph[min(u,v)][max(u,v)]=0
                    deg[u]-=1
                    deg[v]-=1
                    dfs_visit(v)
                if deg[u]==0:
                    q=[u]+q
                    return
        dfs_visit(s)
        return q

    return dfs(matrix,degree,0)
