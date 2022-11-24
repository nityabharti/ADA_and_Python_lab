source = int(input("Enter Source Vertex: "))
num_vertices = int(input("Enter Number of vertices: "))
num_edges = int(input("Enter Number of edges: "))

adjacency_matrix = [[0 for _ in range(num_vertices)]
                    for __ in range(num_vertices)]

result = []


def print_adjacency_matrix():
    for row in adjacency_matrix:
        print(row)


for i in range(num_edges):
    s, d = (int(x)
            for x in input("Enter source, destination (s d): ").split(" "))
    adjacency_matrix[s][d] = 1
    adjacency_matrix[d][s] = 1


def hamiltonion_cycle(matrix, source, vertices, visited, path=[]):
    path.append(source)

    if vertices == 1:
        s = path[0]
        if matrix[source][s]:
            result.append(path+[s])
        path.pop()
        return

    for nxt in range(num_vertices):
        if not visited[nxt] and matrix[source][nxt]:
            visited[nxt] = True
            hamiltonion_cycle(matrix, nxt, vertices-1, visited, path)
            visited[nxt] = False
    path.pop()


print("The Graph is ")
print_adjacency_matrix()

visited = [False for _ in range(num_vertices)]
visited[source] = True

hamiltonion_cycle(adjacency_matrix, source, num_vertices, visited)

print("The Hamiltonian Cycles are: ")
for path in result:
    print(path)