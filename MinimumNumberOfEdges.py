class Graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.edges=[]
		self.queue=[]
		for i in range(self.noOfVertices+1):
			self.edges.append([False])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)
		self.edges[v2].append(v1)

	def bfs(self,v,u):
		if v==u:
			return 0
		else:
			self.queue.append((v,0))
			for q in self.queue:
				vertex=q[0]
				distance=q[1]
				for ver in self.edges[vertex][1:]:
					if not self.edges[ver][0]:
						self.edges[ver][0]=True
						if ver!=u:
							self.queue.append((ver,distance+1))
						else:
							return distance+1

			return -1

spec=raw_input()
spec=spec.split(' ')
g=Graph(int(spec[0]),int(spec[1]))
for e in range(g.noOfEdges):
	input=raw_input()
	input=input.split(' ')
	i=int(input[0])
	j=int(input[1])
	g.addEdges(i,j)
	
path=raw_input()
path=path.split(' ')
print g.bfs(int(path[0]),int(path[1]))
