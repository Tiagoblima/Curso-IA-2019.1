from searchs import bfs_search, dfs_search
from supervised_learn import *
from search_util import Graph


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
result = bfs_search.bfs(g)
print(result)

print("---------------------DFS------------------------")
result = dfs_search.dfs(g)
print(result)

