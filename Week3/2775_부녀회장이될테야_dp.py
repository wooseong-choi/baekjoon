t = int(input())

li = [ [_ if j==0 else 0 for _ in range(15)] for j in range(t+1) ]

# print( li )

for i in range(1,len(li)):
    for j in range(len(li[i])):
        if li[i][j] == 0 :
            sum = 0
            for k in range(j+1):
                sum += li[i-1][k]
            li[i][j] = sum

for i in range(t):
    k = int(input())
    n = int(input())
    print(li[k][n])
