def bfs(graph, s):
    q=deque()
    visited = [False for _ in range(len(graph))]
    Tab_Distance = [-1 for _ in range(len(graph))]

    q.put(s)
    visited[s] = True
    distance=0
    while len(q)!=0:
        distance+=1
        for _ in range(len(q)):
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    Tab_Distance=distance
                    q.put(v)
