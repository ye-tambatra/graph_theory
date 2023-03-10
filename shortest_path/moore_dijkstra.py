def mooreDijkstra(graph, source):
    # Init
    n = len(graph)
    proceeded = [False] * n
    predecessors = [None] * n
    distances = [float("inf")] * n
    distances[source] = 0

    while False in proceeded:
        # Select the vertex that has minimum distance of non proceeded vertices
        min = -1
        for i in range(n):
            if not proceeded[i] and (distances[i] < distances[min] or min == -1):
                min = i

        # Mark the selected vertex as proceeded
        proceeded[min] = True

        for i in range(n):
            # Negative distances not supported
            if graph[min][i] < 0:
                raise Exception("Negative distance detected. No solution")
            # Updating distances and predecessors
            if graph[min][i] != 0 and distances[i] > distances[min] + graph[min][i]:
                distances[i] = distances[min] + graph[min][i]
                predecessors[i] = min

    return (distances, predecessors)
