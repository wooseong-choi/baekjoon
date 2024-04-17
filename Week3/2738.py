n,m = map(int, input().split())
li1 = [[] for _ in range(n)]
li2 = [[] for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    li1[i] = list(map(int, input().split()))
for i in range(n):
    li2[i] = list(map(int, input().split()))

for i in range(n):    
    for j in range(m):
        result[i][j] = li1[i][j] + li2[i][j]

for i in range(n):
    for j in range(m):
        print(result[i][j] ,end=' ')
    print('')