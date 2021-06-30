def sort_dfs2(graph):
    visited = [False]*len(graph)
    resualt=[]
    Q=deque()

    def dfs_visit_2(u):
        nonlocal  graph,visited
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit_2(v)
        Q.appendleft(u)

    for i in range(len(graph)):
        if visited[i]==False:
            dfs_visit_2(i)
    print(Q)
