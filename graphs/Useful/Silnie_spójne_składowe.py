def strong(graph):
    def dfs_visit(u):
        nonlocal graph, visited,Tab_Times,time
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)
        time+=1
        Tab_Times[u]=time
    def dfs_visit2(u):
        nonlocal graph_reverse,visited,Resualt
        visited[u] = True
        Resualt[max(len(Resualt)-1,0)]+=[u]
        for v in graph_reverse[u]:
            if not visited[v]:
                dfs_visit2(v)
    graph_reverse=[]
    for i in range(len(graph)):
        graph_reverse+=[[]]
    for i in range(len(graph)):
        for j in graph[i]:
            graph_reverse[j]+=[i]
            print(j,i,graph_reverse,graph[i])
    print()
    print(graph_reverse)
    visited = [False for _ in range(len(graph))]
    Tab_Times= [-1 for _ in range(len(graph))]
    time=0
    for i in range(len(graph)):
        if  not visited[i]:
            dfs_visit(i)
    q=PriorityQueue()

    for i in range(len(Tab_Times)):
        q.put([-Tab_Times[i],i])
    Resualt=[]
    visited = [False for _ in range(len(graph))]
    while not q.empty():
        current=q.get()
        if  not visited[current[1]]:
            Resualt+=[[]]
            dfs_visit2(current[1])
    print(Resualt)
