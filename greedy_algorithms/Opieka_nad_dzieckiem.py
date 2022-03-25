def opieka(Array):
	q=PriorityQueue()
	n=len(Array)
	#0 zadaniem zajmuje się Cerseri
	#1 zadaniem zajmuje się Jaime
	Plan=[-1 for _ in range(n)]
	Free=[-1,-1]
	for i in range(n):
		q.put([Array[i][0],n])
		q.put([Array[i][1],Array[i][0]])
	index=0
	while not q.empty():
		current=q.get()
		# print("====")
		# print("Plan: ",Plan)
		# print("Free: ",Free)
		# print("Current: ",current)
		if current[1]==n:
			if Free[0]==-1:
				Plan[index]=0
				Free[0]=current[0]
				index+=1
			elif Free[-1]==-1:
				Plan[index]=1
				Free[1]=current[0]
				index+=1
			else:
				print("Nima tak")
				return False
		else:
			if Free[0]==current[1]:
				Free[0]=-1
			else:
				Free[1]=-1
	print(Plan)
	return True


Tab=[[2,4],[3,4],[5,7],[6,8],[11,12],[10,20],[17,18],[30,30]]
opieka(Tab)
