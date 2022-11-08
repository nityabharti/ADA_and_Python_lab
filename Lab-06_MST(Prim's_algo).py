# Write a function that return the MST using PRIM's Algorithm
import sys     # Library for INT_MAX

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                       for row in range(vertices)]


    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i],"-", i, self.graph[i][parent[i]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree  
    def MinKey(self,key,MSTSet):

        # initialize the minimum value 
        min = sys.maxsize      

        for v in range(self.V):
            if key[v] < min and MSTSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V      # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        MSTSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.MinKey(key, MSTSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            MSTSet[u] = True

            # Update distance value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Upd

                if self.graph[u][v] > 0 and MSTSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    
        self.printMST(parent)

if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 10, 7, 0, 5],
               [19, 0, 5, 8, 2],
               [5, 3, 0, 2, 6],
               [0, 7, 1, 0, 2],
               [0, 2, 9, 1, 0]]
    g.primMST() 