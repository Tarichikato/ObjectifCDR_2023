
from collections import defaultdict

def init_graph():

    edges = [["750,250", "250,750"], ["750,250", "750,750"],
        ["750,250", "1750,750"], ["250,750", "250,1250"],
        ["250,750", "750,750"], ["1750,750", "1250,1250"],
        ["1750,750", "1250,2250"], ["250,1250", "750,750"]]
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph

def find_shortest_path(start,goal,graph):

    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return(new_path)
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return