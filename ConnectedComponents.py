class graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.edges=[]
		self.cc=[]
		for i in range(self.noOfVertices+1):
			self.edges.append([False])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)
		self.edges[v2].append(v1)

	def getConnectedComponents(self):
		count=0
		for ver in range(1,self.noOfVertices+1):
			if not self.edges[ver][0]:
				self.cc.append([])
				self.explore(ver,count)
				count +=1
		return count

	def explore(self,ver,count):
		self.cc[count].append(ver)
		self.edges[ver][0]=True
		for v in self.edges[ver][1:]:
			if not self.edges[v][0]:
				self.explore(v,count)

spec=raw_input()
g=graph(int(spec[0]),int(spec[-1]))
for e in range(g.noOfEdges):
	input=raw_input()
	i=int(input[0])
	j=int(input[-1])
	g.addEdges(i,j)
	
print g.getConnectedComponents()
print g.cc
