from collections import defaultdict
import dfs_search
import bfs_search


class Graph():
    def __init__(self, start, end):
        self.edges = defaultdict(list)

    def add_edge(self, source, destination, cost):
        self.edges[source].append((destination, cost))


g = Graph(start='S', end='G')

g.add_edge('S', 'A', 2)
g.add_edge('S', 'B', 1)
g.add_edge('S', 'G', 9)
g.add_edge('A', 'C', 2)
g.add_edge('A', 'D', 3)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 4)
g.add_edge('C', 'G', 4)
g.add_edge('D', 'G', 4)


print("---------------------BFS------------------------")
bfs_search.bfs(g)


print("---------------------DFS------------------------")
dfs_search.dfs(g)

