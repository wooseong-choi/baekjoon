n, m = map(int, input().split())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input()))

visited = [[False] * m for _ in range(n)]

# print(arr)
# print(visited)
que = []
cnt = 0

def bfs(graph, start, visit):
    global cnt
    que.append(start)
    visit[start[0]][start[1]] = True
    while que:
        val = que.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = val[0] + dx, val[1] + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0 or visit[nx][ny]:
                continue
            que.append((nx, ny))
            visit[nx][ny] = True
            graph[nx][ny] = graph[val[0]][val[1]] + 1
            cnt += 1

bfs(arr, (0, 0), visited)
print(arr[n-1][m-1])