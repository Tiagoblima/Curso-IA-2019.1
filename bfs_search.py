from collections import defaultdict


def bfs(g, start='S', end='G'):
    visited = []
    queue = [start]

    for source in queue:

        print(source + "->", end="")
        frontier = g.edges[source]
        print(frontier)

        if frontier is not None:
            for node in frontier:
                if node not in visited:
                    visited.append(node)
                    queue.append(node[0])

    # for node in visited:
    # print(node, "->", end="")
