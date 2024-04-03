n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(1,m+1):
    go, to = map(int, input().split())
    arr[go].append(to)
    indegree[to] +=1 

# print(arr)
# print(indegree)

from collections import deque
que = deque()

# for i in range(1, n+1):
#     if indegree[i] == 0 : que.append(i)

# while que :
#     if indegree[i] == 0:
#         que.append(i)
#         for j in arr[i]:
#             indegree[j] -= 1
result = []
# while que :
for i in range(1,n+1):
    if indegree[i] == 0:
        que.append(i)

while que :
    val = que.popleft()
    result.append(val)
    for j in arr[val]:
        indegree[j] -= 1
        if indegree[j] == 0:
            que.append(j)
    # if indegree[val] == 0:
        

for i in result:
    print( i, end=" " )   