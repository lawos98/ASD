def max_extending_path( G, s, t ):
  def make_path(s,t):
    nonlocal Parent,Path
    if t!=s:
      make_path(s,Parent[t])
      Path+=[t]

  n=len(G)
  flow=[-inf]*n
  Parent=[-1]*n
  flow[s]=inf
  Q=PriorityQueue()
  Q.put([inf,s])
  while not Q.empty():
    vertex=Q.get()
    u=vertex[1]
    for v,f in G[u]:
      f=min(f,flow[u])
      if f>flow[v]:
        flow[v]=f
        Parent[v]=u
        Q.put([-f,v])

  Path=[]
  if Parent[t]==-1:
    return Path
  Path+=[s]
  make_path(s,t)
  return Path
