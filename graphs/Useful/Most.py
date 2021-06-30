def dfs_bridge(graph):
    visited=[0 for _ in range(len(graph))]
    Tab_Times=[inf for _ in range(len(graph))]
    Tab_Bridges=[inf for _ in range(len(graph))]
    time=0
    Result=[]
    def dfs_visit_bridge(u,parent):
        nonlocal graph, visited,Tab_Times,time,Tab_Bridges,Result
        back=inf
        kid=inf
        visited[u] = 1
        time+=1
        Tab_Times[u]=time
        for v in graph[u]:
            if visited[v]==0:
                dfs_visit_bridge(v,u)
                kid=min(kid,Tab_Bridges[v])
            elif parent!=v:
                back=min(back,Tab_Times[v])
        Tab_Bridges[u]=min(Tab_Times[u],kid,back)
        if Tab_Bridges[u]==Tab_Times[u] and parent!=-1:
            Result+=[[parent,u]]
    for i in range(len(graph)):
        if visited[i]==False:
            dfs_visit_bridge(i,-1)
    print(Result)
