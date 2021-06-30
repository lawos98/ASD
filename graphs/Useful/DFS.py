def dfs(graph,s):
    visited = [False for _ in range(len(graph))]
    Tab_Times_Start= [-1 for _ in range(len(graph))]
    Tab_Times_End= [-1 for _ in range(len(graph))]
    time=0
    def dfs_visit(u):
        nonlocal graph, visited,Tab_Times_Start,Tab_Times_End,time
        time+=1
        visited[u] = True
        Tab_Times_Start[u]=time
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)
        time+=1
        Tab_Times_End[u]=time

    dfs_visit(s)
