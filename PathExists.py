class graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.edges=[]
		for i in range(self.noOfVertices+1):
			self.edges.append([False])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)
		self.edges[v2].append(v1)

	def doesPathExist(self,v1,v2):
		if v2 in self.edges[v1]:
			return 1
		else:
			for v in self.edges[v1]:
				if not self.edges[v][0]:
					self.edges[v][0]=True
					if self.doesPathExist(v,v2)==1:
						return 1
						break
			return 0

spec=raw_input()
g=graph(int(spec[0]),int(spec[-1]))
for e in range(g.noOfEdges):
	input=raw_input()
	i=int(input[0])
	j=int(input[-1])
	g.addEdges(i,j)

path=raw_input()
path=g.doesPathExist(int(path[0]),int(path[-1]))
print path
