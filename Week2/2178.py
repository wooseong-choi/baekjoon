n,m = map(int, input().split())

arr = [[] for _ in range(n+1)]
for i in range(1,n+1):
    for j in input():
        arr[i].append(j)


visited = [False] * (n+1)

que = []
cnt = 0
def bfs(graph, start, visit):
    que.append(start)
    visit[start] = True
    while que:
        val = que.pop(0)
        # print(val)
        for i in graph[val]:
            print(visit)
            if int(i) == 0: break
            if not visit[int(i)]:
                que.append(int(i))
                visit[int(i)] = True
                cnt += 1


bfs(arr, 1, visited)