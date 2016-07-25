class graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.indegree=[]
		self.edges=[]
		self.topologicalOrder=[]
		for i in range(self.noOfVertices+1):
			self.edges.append([False])
			self.indegree.append([])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)
		self.indegree[v2].append(v1)

	def getTopologicalSort(self):
		for v in range(1,self.noOfVertices+1):
			if not self.edges[v][0]:
				self.dfs(v)

		return self.topologicalOrder[::-1]

	def dfs(self,v):
		self.edges[v][0]=True
		for ver in self.edges[v][1:]:
			if not self.edges[ver][0]:
				self.dfs(ver)

		if len(self.edges[v])<2:
					self.topologicalOrder.append(v)
					for i in self.indegree[v]:
						self.edges[i].remove(v)
					self.indegree[v]=[]

spec=raw_input()
spec=spec.split(' ')
g=graph(int(spec[0]),int(spec[1]))
for e in range(g.noOfEdges):
	input=raw_input()
	input=input.split(' ')
	i=int(input[0])
	j=int(input[1])
	g.addEdges(i,j)

print g.getTopologicalSort()
