# undirected graph, unweighted graph
class Graph:
    def __init__(self):
        self.graph = {}  # Storing graph as an adjacency list
        self.num_vertices = 0

    def add_edge(self, s, d):
        if s in self.graph:
            self.graph[s].append(d)
        else:
            self.num_vertices += 1
            self.graph[s] = [d]

        # since it is undirected
        if d in self.graph:
            self.graph[d].append(s)
        else:
            self.num_vertices += 1
            self.graph[d] = [s]

    def display(self):
        for key in self.graph.keys():
            print(f"{key} -> {self.graph[key]}")

    # Depth First Search
    def dfs(self, source):
        visited = {}
        for key in self.graph.keys():
            visited[key] = False

        self.__dfs_helper(source, visited)

    # Function to make recursive calls
    def __dfs_helper(self, source, visited):
        if visited[source]:
            return
        visited[source] = True
        print(source, end=" -> ")
        for nxt in self.graph[source]:
            self.__dfs_helper(nxt, visited)

    # Breadth First Search
    def bfs(self, source):
        visited = {}
        for key in self.graph.keys():
            visited[key] = False

        q = [source]
        visited[source] = True

        while (len(q) != 0):
            cur_node = q.pop(0)
            print(cur_node, end=" -> ")

            for nxt in self.graph[cur_node]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True


if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter Number of edges: "))
    for i in range(num_edges):
        s, d = tuple(input("Enter s,d: ").split(" "))
        g.add_edge(s, d)

    print("The Graph: ")
    g.display()

    source = input("Enter source vertex: ")
    print("\nThe Depth First Search Traversal is")
    g.dfs(source)
    print()
    print("\nThe Breadth First Search Traversal is")
    g.bfs(source)