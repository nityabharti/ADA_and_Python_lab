# Edge list to adjacency list of weighted undirected graph
class Graph:
    # constructor
    def __init__(self):
        self.adjacency_list = {}

    # method to add edges
    def add_edge(self, v1, v2, w=1):
        if v1 in self.adjacency_list:
            self.adjacency_list[v1].append((v2, w))
        else:
            self.adjacency_list[v1] = [(v2, w)]

        if v2 in self.adjacency_list:
            self.adjacency_list[v2].append((v1, w))
        else:
            self.adjacency_list[v2] = [(v1, w)]

    # method to display the adjacency list
    def display(self):
        for vertex in self.adjacency_list.keys():
            print(f"{vertex} -> {self.adjacency_list[vertex]}")


if __name__ == "__main__":

    v = int(input("Enter Number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    print("\nStart entering edges (s,d,w): ")
    edges = [list(map(int, input().split(" "))) for i in range(num_edges)]

    # Graph Object
    g = Graph()

    # Adding all the edges
    for edge in edges:
        v1, v2, w = edge
        g.add_edge(v1, v2, w)

    print("\nAdjacency List is: ")
    g.display()