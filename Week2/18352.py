from collections import deque
import sys
f = sys.stdin.readline

n , m , k , x = map(int, f().split())

li = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(1,m+1):
    ffrom, to = map(int,f().split()) 
    li[ffrom].append( to)

# print(li)
# print(visited)

city = [0] * (n+1)

# print(city)


def bfs(graph, start, visit):
    
    visit[start] = True
    que = deque([start])
    while que:
        val = que.popleft()
        # city[val] = city[val]+1
        # print(val)
        for i in graph[val]:
            if not visit[i]:
                que. append(i)
                visit[i] = True
                city[i] = int(city[val])+1

bfs(li, x, visited)

# print(city)
result = ''
for i,val in enumerate(city):
    if val == k:
        result = result + str(i)+' '

if len(result) == 0:
    print('-1')
else:
    for i in result.split():
        print(i)

    