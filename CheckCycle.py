class Graph:
	def __init__(self,ver,edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.edges=[]
		for i in range(self.noOfVertices+1):
			self.edges.append([False])

	def addEdges(self,v1,v2):
		self.edges[v1].append(v2)

	def checkCycle(self):
		cycle=False
		discover=[False for i in range(self.noOfVertices+1)]
		for v in range(1,self.noOfVertices+1):
			if not self.edges[v][0]:
				self.edges[v][0]=True
				discover1=[]
				discover1.extend(discover)
				cycle=self.explore(v,discover1)
				if cycle:
					return cycle

		return cycle

	def explore(self,ver,discover):
		discover[ver]=True
		cycle=False
		for v in self.edges[ver][1:]:
			if not discover[v]:
				cycle=self.explore(v,discover)
				if cycle:
					return cycle
				else:
					cycle=False
			else:
				cycle=True
				return cycle
			discover[v]=False

		return cycle


spec=raw_input()
spec=spec.split(' ')
g=Graph(int(spec[0]),int(spec[1]))
for e in range(g.noOfEdges):
	input=raw_input()
	input=input.split(' ')
	i=int(input[0])
	j=int(input[1])
	g.addEdges(i,j)

print g.checkCycle()
