n, k = map(int, input().split())

li =[ [0 for i in range(k+1)] for j in range(n+1) ] 
# li2 =[ [False for i in range(k+1)] for j in range(n+1) ] 

w = []
v = []

# print( li )

for i in range(n):
    temp_w, temp_v = map(int, input().split())
    w.append(temp_w)
    v.append(temp_v)

# print(w)
# print(v)
# i == 가치 
# j == 무게

for i in range(1, len(li)):
    for j in range(1, len(li[i]) ):
        if j < w[i-1] : li[i][j] = li[i-1][j]
        if j >= w[i-1]:
            li[i][j] = v[i-1] + li[i-1][j-w[i-1]] 

        li[i][j] = max(li[i][j], li[i-1][j] )



# def dfs( li, i, val, visited ):
#     visited[i][val] = True
#     for i_ in range(1, len(li)):
#         for j_ in range(1,len(li[i_])):
#             if not visited[i_][j_]: 
#                 visited[i_][j_] = False
#                 if j_ < w[i_-1] : li [i_][j_] = li[i_-1][j_]
#                 if j_ >= w[i_-1]:
#                     li[i_][j_] = v[i_-1] + li[i_-1][j_-w[i_-1]] 
                
#                 li[i_][j_] = max(li[i_][j_], li[i_-1][j_] )
#                 dfs(li, i_, j_ , visited)
            
# dfs(li, 1,1, li2)
print(li[n][k])

# for i in li:
#     print(i)