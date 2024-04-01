n,m,v = map(int, input().split())

arr = [[] for _ in range(n+1)]



def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)
    
que = []
def bfs(graph, start, visited):
    que.append(start)
    visited[start] = True
    
    while que:
        val = que.pop(0)
        print(val, end=" ")
        for i in graph[val]:
            if not visited[i]:
                que.append(i)
                visited[i] = True



dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for i in range(m):
    # print(i+1)
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

#print(arr)


dfs(arr, v, dfs_visited)
print()
bfs(arr, v, bfs_visited)