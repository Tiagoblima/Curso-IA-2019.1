from collections import defaultdict
from search_util import Queue


def bfs(g, start='S', end='G'):
    parent = {start: None}
    queue = Queue()
    visited = []
    queue.push(start)

    while not queue.is_empty():

        source = queue.pop()
        frontier = g.edges[source]

        if frontier is None:

            previous = source

            path = []
            while parent[previous] is not None:
                node = parent[previous]
                previous = node[0]

            path.reverse()
            return path

        for node in frontier:
            if node not in visited:
                parent[node[0]] = source
                visited.append(node)
                queue.push(node)

    # for node in visited:
    # print(node, "->", end="")
