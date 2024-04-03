from collections import deque

n = int(input())  # 부품의 수
m = int(input())  # 간선의 수

# arr[i] = (to, cost) 형태로 저장될 것임
arr = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    to, go, cost = map(int, input().split())
    arr[go].append((to, cost))  # 가중치와 목적지
    indegree[to] += 1

que = deque()

# 최초 기본 부품들을 큐에 입력
for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

result = [0] * (n + 1)  # 부품의 비용을 담을 배열

while que:
    val = que.popleft()
    for to, cost in arr[val]:
        result[to] = result[to]+result[val] + cost  # 누적 비용 중 최대값 저장
        indegree[to] -= 1
        if indegree[to] == 0:
            que.append(to)

# result 배열에서 0번째 인덱스는 사용하지 않으므로 제외하고 출력
print(result[1:])
