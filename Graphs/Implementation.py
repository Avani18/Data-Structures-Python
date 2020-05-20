#Implementation of Graph from the scratch using dictionary

#Class for Graph
class Graph:
	
	def __init__(self, graph_dict = None):
		#Initialise graph dictionary
		self.__graph_dict = graph_dict
		
	#Function to get list of vertices
	def vertices(self):
		return list(self.__graph_dict.keys())
		
	#Function get set of edges
	def edges(self):
		return self.__generate_edges()
		
	#Function to add a vertex to the graph
	def add_vertex(self, vertex):
		#If vertex does not exist
		if vertex not in self.__graph_dict:
			#Add vertex with an empty list for its neighbours
			self.__graph_dict[vertex] = []
			
	#Function to add edge 
	#This function takes a set input as parameter
	def add_edge(self, edge):
		#Get edge in set form (ascending order)
		edge = set(edge)
		#Get values of vertex1 and vertex2 using tuple
		(vertex1, vertex2) = tuple(edge)
		#If vertex1 exists
		if vertex1 in self.__graph_dict:
			#Append vertex2 to its list of neighbours
			self.__graph_dict[vertex1].append(vertex2)
		else:
			#Create a new vertex with vertex1 and add vertex2 to its neighbour list
			self.__graph_dict[vertex1] = [vertex2]
			
	#Function to generate the edges
	def __generate_edges(self):
		#Empty list
		edges = []
		
		#Iterate over each vertex
		for vertex in self.__graph_dict:
			#Iterate over each neighbour of the vertex
			for neighbour in self.__graph_dict[vertex]:
				#If edge has not been added already
				if {neighbour, vertex} not in edges:
					#Add edge to list
					edges.append({vertex, neighbour})
		return edges
		
	#Function to print graph
	def __str__(self):
		#String for vertices
		res = 'vertices: '
		for k in self.__graph_dict:
			res += str(k) + ' '
		#Add string for edges
		res += '\nedges: '
		for edge in self.__generate_edges():
			res += str(edge) + ' '
		return res
		
		
'''g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }'''
        
g = { '0' : ['1', '4'],
		'1' : ['0', '2', '3', '4'],
		'2' : ['1', '3'],
		'3' : ['1', '2', '4'],
		'4' : ['0', '1', '3']
		}
graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print("Add vertex:")
graph.add_vertex("z")

print("Vertices of graph:")
print(graph.vertices())
 
print("Add an edge:")
graph.add_edge({"a","z"})
    
print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})

print("Vertices of graph:")
print(graph.vertices())
print("Edges of graph:")
print(graph.edges())
