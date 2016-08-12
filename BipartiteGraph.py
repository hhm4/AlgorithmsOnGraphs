class Graph:

	def __init__(self, ver, edg):
		self.noOfVertices=ver
		self.noOfEdges=edg
		self.bipartite=True
		self.edges=[]
		self.vertexColors=[]
		for i in range(ver+1):
			self.edges.append([])
			self.vertexColors.append(0)
	
	def colorVertices(self):
		for v in range(1,self.noOfVertices+1):
			color=self.vertexColors[v]
			if color==0:
				self.vertexColors[v]=1
				if self.colorEdges(v,2):
					pass
				else:
					break

			else:
				pass
				
	def colorEdges(self,ver,color):
		for e in self.edges[ver]:
			ecolor=self.vertexColors[e]	
			if ecolor==0:
				self.vertexColors[e]=color
			else:
				if ecolor==color:
					pass
				else:
					self.bipartite=False
					break;

		if self.bipartite:
			for e in self.edges[ver]:
				if self.vertexColors[e]==1:
					self.colorEdges(e,2)
				else:
					self.colorEdges(e,1)



input=raw_input()
input=input.split(' ')
g=Graph(int(input[0]),int(input[1]))
for i in range(1,g.noOfEdges+1):
	edge=raw_input()
	edge=edge.split(' ')
	g.edges[int(edge[0])].append(int(edge[1]))

g.colorVertices()
if g.bipartite:
	print '1' 
else: 
	print '0'
	
