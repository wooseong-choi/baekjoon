n , m = map(int, input().split())

nxm_arr = [ [] for _ in range(n+1) ]
nxm_parent = [ [] for _ in range(n+1) ]

for j in range(1,m+1):
    a = input()
    # print(a)
    a_ = list(a)
    nxm_arr[j]= a_
    nxm_parent[j] = list( False for _ in range(len(a_)))

# print(nxm_arr)
# print(nxm_parent)

# def union(list, x, y):
#     find_x = find(list,x)
#     find_y = find(list,y)

#     if find_x == find_y : return 
#     if find_x < find_y : list[find_y] = list[find_x]
#     else : list[find_x] = list[find_y] 


# def find(list, x):
#     if list[x] == x : return x 
#     return find(list, list[x])

# for i in range(1, n+1):
#     # 세로
#     for j in range(1, m+1):
#         # 가로
#         if j > 1:
#             union( nxm_parent, nxm_arr[i][j-1], nxm_arr[i][j])
        
#         print(nxm_parent)
cnt = 0
local_cnt = 0
def dfs(graph, x_start, y_start ,mode,  visited):
    global cnt
    global local_cnt
    visited[x_start][y_start] = True
    if mode == '-':
        for i,v in enumerate(graph[x_start]) :
            if not visited[x_start][i] :
                
                if v == '-' : 
                   local_cnt +=1 
                   if local_cnt == len(graph[x_start]) : 
                       local_cnt = 0
                       cnt +=1

                elif v == '|' and local_cnt > 0 : 
                    local_cnt = 0 
                    cnt += 1
                
                visited[x_start][i] = True
                print(local_cnt, len(graph[x_start]))
                
                dfs(graph, x_start, i, mode, visited)
        
    else:
        pass

for i in range(1, n+1):
    for j in range(m):
        # print(i, j)
        dfs(nxm_arr, i, j , '-', nxm_parent)

print(cnt)