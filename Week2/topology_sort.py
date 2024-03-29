import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수와 간선의 개수를 입력 받기
n,m =  map(int, input().split())

# 모든 노드에 대한 진입 차수 0으로 초기화
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(n+1)]

# 방향 그래프의 모든 간선정보를 입력 받기
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b) # 정점 A 에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

print(graph)

def topology_sort():
    result =[]
    que = deque()

    for i in range(1,n+1):
        # 진입차수가 0인 정점이라면
        if indegree[i] == 0:
            que.append(i)

    while que:
        current = que.popleft()
        result.append(current)

        for i in graph[current]:
            # current로부터 나가는 간선 제거
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)

    
    for i in result:
        print(i, end=' ')

topology_sort()