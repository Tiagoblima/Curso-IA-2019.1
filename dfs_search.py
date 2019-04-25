from collections import defaultdict


def dfs(g, start='S', end='G'):
    visited = []
    frontier = [start]
    stack = frontier

    first_frontier = g.edges[start]

    while len(frontier) > 0:

        source = stack[len(stack) - 1]
       

        frontier = g.edges[source[0]]
        print(source + "->" + "{0}".format(frontier))
        stack.remove(source[0])

        if frontier is not None:
            for node in frontier:

                if node not in visited:
                    visited.append(node)
                    stack.append(node[0])

 
