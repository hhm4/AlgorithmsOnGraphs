class Graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.indegree=[]
		self.edges=[]
		self.rEdges=[]
		self.rIndegree=[]
		self.rTopologicalOrder=[]
		self.SCC=[]

		for i in range(self.noOfVertices+1):
			self.edges.append([False])
			self.indegree.append([])
			self.rEdges.append([False])
			self.rIndegree.append([])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)
		self.indegree[v2].append(v1)
		self.rEdges[v2].append(v1)
		self.rIndegree[v1].append(v2)

	def getTopologicalSort(self):
		for v in range(1,self.noOfVertices+1):
			if not self.rEdges[v][0]:
				self.rDfs(v)

		self.rTopologicalOrder=self.rTopologicalOrder[::-1]

	def rDfs(self,v):
		self.rEdges[v][0]=True
		for ver in self.rEdges[v][1:]:
			if not self.rEdges[ver][0]:
				self.rDfs(ver)

		self.rTopologicalOrder.append(v)
		for i in self.rIndegree[v]:
			self.rEdges[i].remove(v)
		self.rIndegree[v]=[]

	def dfs(self,v,discover):
		self.edges[v][0]=True
		for ver in self.edges[v][1:]:
			if not self.edges[ver][0]:
				self.dfs(ver,discover)

		discover.append(v)
		for i in self.indegree[v]:
			self.edges[i].remove(v)
		self.indegree[v]=[]

	def getStronglyConnectedComponents(self):
		for v in self.rTopologicalOrder:
			if not self.edges[v][0]:
				self.edges[v][0]=True
				discover=[]
				self.dfs(v,discover)
				self.SCC.append(discover)


spec=raw_input()
spec=spec.split(' ')
g=Graph(int(spec[0]),int(spec[1]))
for e in range(g.noOfEdges):
	input=raw_input()
	input=input.split(' ')
	i=int(input[0])
	j=int(input[1])
	g.addEdges(i,j)

g.getTopologicalSort()
g.getStronglyConnectedComponents()
print len(g.SCC)
print g.SCC
