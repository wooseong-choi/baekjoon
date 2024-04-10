n = int(input())
li = [[0 for _ in range(n)] for _ in range(n)]

# print(len(li))
arr = []
for _ in range(n):
    r,c = map(int, input().split())
    arr.append((r,c))


for i in range(1,n):
    # print ( i)
    # r,c = map(int, input().split())
    # li[i][i] = (r,c)

    # if i > 0:
    #     pre_r,pre_c = li[i-1][i-1] # A
    #     li[i-1][i] = pre_r * r * c # (AB)
    # if i > 1:
    #     ab = li[i-2][i-1] # (AB)
    #     a_r, a_c = li[i-2][i-2] # A
    #     b_r, b_c = li[i-1][i-1] # B
    #     c_r, c_c = li[i][i] # C

    #     abc = ab+(a_r * c_r * c_c) # (AB)C

    #     bc = li[i-1][i] # (BC)

    #     bca = bc+(a_r * b_r * c_c) # (BC)A

    #     li[i-2][i] = min(abc, bca) # (BC)A
    for j in range(n-i):
        x,y = j, j+i
        li[x][y] = min (  
            li[x][y-1]+ arr[x][0]*arr[y][0]*arr[y][1],
            li[x-1][y]+ arr[x][0]*arr[x][1]*arr[y][1]
         )
        print(li[x][y-1], arr[x][0],arr[y][0],arr[y][1])

# for k in range(1,n):
#     for i in range(n-k):
#         x,y = i, i+k
#         li[x][y] = min(0 if isinstance(li[x][y-1],tuple) else li[x][y-1]  +li[x][x][0]*li[y][y][0]*li[y][y][1],0 if isinstance(li[x-1][y],tuple) else li[x-1][y] +li[x][x][0]*li[x][x][1]*li[y][y][1] )


print(li[0][n-1])
for idx,i in enumerate(li):
    if idx < 11:
        print(i)
