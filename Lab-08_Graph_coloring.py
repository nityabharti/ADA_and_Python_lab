# program to find the minimum number of colors needed to color the graph
from collections import deque
 
# Function to count the minimum
# number of color required
def minimumColors(N, E, U, V):
 
    # Create array of vectors
    # to make adjacency list
    adj = [[] for i in range(N)]
 
    # Initialise colors array to 1
    # and count array to 0
    count = [0]*N
    colors = [1]*(N)
 
    # Create adjacency list of
    # a graph
    for i in range(N):
        adj[V[i] - 1].append(U[i] - 1)
        count[U[i] - 1] += 1
 
    # Declare queue Q
    Q = deque()
 
    # Traverse count[] and insert
    # in Q if count[i] = 0
    for i in range(N):
        if (count[i] == 0):
            Q.append(i)
 
# Traverse queue and update
    # the count of colors
    # adjacent node
    while len(Q) > 0:
        u = Q.popleft()
 
        # Traverse node u
        for x in adj[u]:
            count[x] -= 1
 
            # If count[x] = 0
            # insert in Q
            if (count[x] == 0):
                Q.append(x)
 
            # If colors of child node is less than
            # parent node, update the count by 1
            if (colors[x] <= colors[u]):
                colors[x] = 1 + colors[u]
 
    # Stores the minimumColors
    # requires to color the graph.
    minColor = -1
 
    # Find the maximum of colors[]
    for i in range(N):
        minColor = max(minColor, colors[i])
# Print the minimum no. of colors required.
    print(minColor)
 
# Driver function
N = 5
E = 6
U = [1, 2, 3, 1, 2, 3]
V = [3, 3, 4, 4, 5, 5]
 
minimumColors(N,E,U,V)