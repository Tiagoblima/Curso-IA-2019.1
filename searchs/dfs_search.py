from collections import defaultdict
from search_util import Stack


def dfs(g, start='S', end='G'):
    parent = {start: None}
    visited = []
    stack = Stack()
    stack.push(start)

    while not stack.is_empty():

        source = stack.pop()

        frontier = g.edges[source[0]]
        print(frontier)

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
                stack.push(node)
