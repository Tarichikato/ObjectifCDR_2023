# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph

from collections import defaultdict


# Class to represent a graph
class Graph:

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # Function to print shortest path
    # from source to j
    # using parent array
    def printPath(self, parent, j,l):

        # Base Case : If j is source
        if parent[j] == -1:
            print(j)
            l += [j]
            print(l)
            return(l)
        l += [j]
        self.printPath(parent, parent[j],l)

        print(j)

    def getPath(self, parent, j,l):

        # Base Case : If j is source
        if parent[j] == -1:
            l += [j]
            self.path = l[::-1]
            return
        l += [j]
        self.getPath(parent, parent[j],l)


    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            #print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
            l = []
            self.printPath(parent, i,l)

    def getSolution(self, dist, parent,goal):
        src = 0
        for i in range(1, len(dist)):
            if(i == goal):
                l = []
                self.getPath(parent, i,l)


    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''

    def dijkstra(self, graph, src,goal):

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        # Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

        # Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist, queue)
            if(u == -1):
                break
            #print(u)

            # remove min element
            #print(u)
            if u in (queue):
                queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        # print the constructed distance array

        self.getSolution(dist, parent,goal)



def find_shortest_path(start,goal,adj,nodes):
    s = nodes.index(start)
    go = nodes.index(goal)
    g = Graph()
    g.dijkstra(adj,s,go)
    p = []
    for n in g.path:
        p+=[nodes[n]]
    return(p)

def init_graph():
    space = 250
    g = Graph()
    graph = []
    nodes = []
    N = 3000//space + 1
    n = 2000//space + 1
    for i in range(n):
        for k in range (N):
            edges = [0]*(N*n)
            j = i * N + k
            if(k == 0):
                if (i == 0):
                    edges[j + N] = 10
                    edges[j + 1] = 10
                    edges[j + N + 1] = 14
                elif (i == n - 1):
                    edges[j - N] = 10
                    edges[j + 1] = 10
                    edges[j - N + 1] = 14
                else:
                    edges[j - N] = 10
                    edges[j + N] = 10
                    edges[j + 1] = 10
                    edges[j - N + 1] = 14
                    edges[j + N + 1] = 14
            elif(k ==N-1):
                if (i == 0):
                    edges[j + N] = 10
                    edges[j - 1] = 10
                    edges[j + N - 1] = 14
                elif (i == n - 1):
                    edges[j - N] = 10
                    edges[j - 1] = 10
                    edges[j - N - 1] = 14
                else:
                    edges[j - N] = 10
                    edges[j + N] = 10
                    edges[j - 1] = 10
                    edges[j - N - 1] = 14
                    edges[j + N - 1] = 14
            else:
                if (i == 0):
                    edges[j + N] = 10
                    edges[j + 1] = 10
                    edges[j - 1] = 10
                    edges[j + N - 1] = 14
                    edges[j + N + 1] = 14
                elif(i == n-1):
                    edges[j - N] = 10
                    edges[j + 1] = 10
                    edges[j - 1] = 10
                    edges[j - N - 1] = 14
                    edges[j - N + 1] = 14
                else:
                    edges[j-N] = 10
                    edges[j+N] = 10
                    edges[j+1] = 10
                    edges[j-1] = 10
                    edges[j - N - 1] = 14
                    edges[j - N + 1] = 14
                    edges[j + N - 1] = 14
                    edges[j + N + 1] = 14

            nodes.append((k * space, i * space))
            graph.append(edges)
    return(graph,nodes)
