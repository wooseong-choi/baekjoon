from collections import defaultdict, deque

# 입력 받기
N = int(input())  # 부품의 수
M = int(input())  # 관계의 수

# 그래프 구성
graph = defaultdict(list)  # 그래프 정보를 저장할 defaultdict
in_degree = [0] * (N + 1)  # 각 부품의 진입 차수를 저장할 리스트
needed_basic_components = [0] * (N + 1)  # 각 기본 부품의 필요 개수를 저장할 리스트

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # 중간 부품으로부터의 간선 정보 저장
    in_degree[X] += 1

# 위상 정렬 수행
queue = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()

    # 부품의 개수를 계산
    for X, K in graph[current]:
        needed_basic_components[X] += K * needed_basic_components[current]
        in_degree[X] -= 1

        if in_degree[X] == 0:
            queue.append(X)

# 결과 출력
for i in range(1, N):
    if not graph[i]:  # 기본 부품일 경우
        print(f"{i}번 부품의 필요 개수: {needed_basic_components[i]}")
