n = int(input())
m = int(input())

arr = [[] for _ in range(n+1) ]
indegree = [0] * (n+1)

from collections import deque

que = deque()
result = [ 0 for _ in range(n)]

for i in range(1,m+1):
    to, go ,cost = map(int, input().split())
    arr[go].append((to, cost)) # 가중치와 목적지 
    indegree[to] += 1  

# 최초 기본 부품들 큐에 입력
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)
print(arr)
print(indegree)
print(que)


while que :
    val = que.popleft()
    # print(val)
    for to, cost in arr[val]:
        print( to, cost)
        # result[val-1] += cost
        temp = 0
        print(arr[to])
        for in_to,in_cost in arr[to]:
            temp += in_cost * cost
        print( temp, cost )
        result[val-1]+= temp * cost
        print(result)
        # result[val-1] = 최종
        indegree[to] -= 1
        if indegree[to] == 0:
            que.append(to)

print(result)