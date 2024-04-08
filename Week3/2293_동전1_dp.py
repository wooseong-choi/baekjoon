# n , k = map(int, input().split())

# li = []

# graph = [ [0 for _ in range(k+1)] for _ in range(n+1) ]

# for i in range(n):
#     li.append(int(input()))


# for i in range(1, len(graph)):
#     for j in range(1,len(graph[i])):
#         if graph[i][j] % li[i-1] == 0 :
#            graph[i][j] += 1

# print(graph)
# print(li)

"""
    동적 계획법은 최적화 문제를 해결하는 알고리즘으로서, 아래의 내용을 항상 명심해야 한다.
    1. '전체의 문제'를 '부분 문제'로 잘 나누었는가? 그렇다면 전체 문제를 해결하기 위한 부분 문제의 점화식은 무엇인가?
    2. 부분 문제들을 해결하며 얻는 결과값을 메모이제이션하는가?
    3. 부분 문제의 점화식은 부분 문제들 사이의 '관계'를 빠짐없이 고려하는가?
"""
"""
    위 내용을 바탕으로 했을 때 2293번의 문제 핵심은 다음과 같다.
    1. '가치의 합이 k원이 되는 경우의 수'를 구하는 전체의 문제를, '가치의 합이 i(1<=i<=k)원이 되는 경우의 수'를 구하는 부분 문제로 나눈다.
    2. 위에서 언급한 부분 문제들을 해결해나가며 메모이 제이션을 할 것인데, 시간제한이 0.5초이며 메모리 제한도 있어서 하나의 리스트 안에서 덮어 씌우는 식으로 빠르게 해결해야 한다.
    3. 입출력 예시로 주어진 경우 말고 다른 예시를 생각해보며 테스티해봐야 한다.
"""


n, k = map(int, input().split())

coins = [] # 코인의 종류
for i in range(n):
    coins.append(int(input()))
coins.sort()

DP = [0] * (k + 1) # 리스트 선언
DP[0] = 1 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언
for c in coins:
    for i in range(c, k + 1):
        DP[i] += DP[i - c]
        # print(c ,DP)
    
print(DP[k])