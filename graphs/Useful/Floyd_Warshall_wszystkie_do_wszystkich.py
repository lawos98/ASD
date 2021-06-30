from math import inf

def Floyd_Warshall(G):
	d=[[inf for _ in range(len(G))] for _ in range(len(G))]
	Parent=[[-1 for _ in range(len(G))] for _ in range(len(G))]
	for v in range(len(G)):
		d[v][v]=0
	for v1 in range(len(G)):
		for v2,w in G[v1]:
			d[v1][v2]=w
			Parent[v1][v2]=v1
	for u in range(len(G)):
		for v1 in range(len(G)):
			for v2 in range(len(G)):
				if d[v1][v2]>d[v1][u]+d[u][v2]:
					d[v1][v2]=d[v1][u]+d[u][v2]
					Parent[v1][v2]=Parent[u][v2]
