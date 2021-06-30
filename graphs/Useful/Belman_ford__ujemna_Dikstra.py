def bellman_ford(E, n, s):
    d = [inf] * n
    d[s] = 0

    for i in range(n - 1):
        for (u, v, w) in E:
            if d[u] + w < d[v]:
                d[v] = d[u] + w

    for (u, v, w) in E:
        if d[v] > d[u] + w:
            return "Ujemny Cykl"

    return d
