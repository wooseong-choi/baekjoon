# g = grapg
# v = visit
# visited = visited
def DFS(g,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited)

g =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]

visited = [False] * 9

DFS(g,1,visited)


from collections import deque

def bfs(graph_bfs, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph_bfs[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph_bfs =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]
visited_bfs = [False] * 9
print()
bfs(graph_bfs,1,visited_bfs)
