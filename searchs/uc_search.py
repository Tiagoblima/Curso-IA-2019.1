from search_util import PriorityQueue


def bfs(g, start='S', end='G'):
    parent = {start: None}
    queue = PriorityQueue()
    visited = []
    queue.push(start, 0)

    while not queue.is_empty():

        source = queue.pop()
        frontier = g.edges[source]
        print(source + "->" + "{0}".format(frontier))

        if frontier is None:
            previous = source
            path = []
            while previous is not None:
                path.append(previous)
                previous = parent[previous]

            path.reverse()
            return path

        if frontier is not None:
            for node in frontier:
                if node[0] not in visited:
                    visited.append(node[0])
                    queue.push(node[0], node[2])
