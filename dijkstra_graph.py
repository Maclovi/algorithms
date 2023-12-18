def dijkstra_graph(graph, start):
    all_vertex = []
    costs = {}
    parents = None
    processed = []

    def find_min_vertex(x): return 1

    node = start
    while node:
        cost = costs[node]
        neighbors = node.links
        for link in neighbors:
            new_cost = cost + link.dist
            vertex = link.v2 if link.v2 != node else link.v1
            if new_cost < costs[vertex]:
                costs[vertex] = new_cost
                costs[vertex] += parents
                costs[vertex] += link

        processed.append(node)
        node = find_min_vertex(all_vertex)
