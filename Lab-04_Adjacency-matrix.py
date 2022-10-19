# Add the vertex to the set of vertices and the graph

def add_vertices(v):
    global graph
    global vertices_no
    global vertices

    if v in vertices:
        print("Vertex", v, "alredy exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        matrix=[]
        for i in range (vertices_no):
            matrix.append(0)
        graph.append(matrix)

# Add an edge betweeen vertex v1 vertex v2 with edge weight W
def add_edge(v1,v2,W):
    global graph
    global vertices_no
    global vertices

    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex", v1, "does not exist.")
    # Check if vertex v2 is a valid vertex
    elif v2 not in vertices:
        print("Vertex", v2, "does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = W


#Print the graph
def Print_Graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], "->", vertices[j], "edge weight:", graph[i][j])

# Store the  vertices of graph
vertices = []
# Store the number of vertiices in the graph
vertices_no = 0
graph = []
# Add the vertices to the graph
add_vertices("A")
add_vertices("B")
add_vertices("C")
add_vertices("D")
add_vertices("E")

# Add  the edges between the vertices by specifying 
# the from and to vertex along with  the edge weights.
add_edge('A','B','5')
add_edge('E','C','7')
add_edge('C','A','9')
add_edge('D','C','3')
add_edge('B','D','1')
add_edge('E','A','2')
add_edge('A','E','4')
add_edge('C','b','8')
add_edge('B','D','6')

Print_Graph()
print("Internal Representation:",graph)