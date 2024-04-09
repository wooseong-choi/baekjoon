n = int(input())
m = int(input())

li = [ [ 0 for _ in range(n+1) ] for _ in range(n+1) ]

dist = [[ 0 for _ in range(n+1)  ] for _ in range(n+1)]

# print(li)
for _ in range(1,m+1):
    k,v = map(int, input().split())
    li[k][v] = v
    # print(li)


INF = 9999999999
# print(INF)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j : dist[i][j] = 0
        elif li[i][j] : dist[i][j] = li[i][j]
        else : dist[i][j] = INF
# print( dist )

def floyde_wadshal(key):
    for k in range(1,key+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


for i in range(1, n+1):
    floyde_wadshal(i)

cnt = 0
for i in range(1,n+1):
    # print((len(dist[i])) - (dist[i].count(INF) + dist[i].count(0)))
    cnt = max(cnt, (len(dist[i])) - (dist[i].count(INF) + dist[i].count(0)) )

print(cnt)

#시간초과 난다 그리고 구현이 틀렸다
