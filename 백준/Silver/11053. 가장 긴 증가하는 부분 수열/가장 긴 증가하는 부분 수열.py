n = int(input())
li = list(map(int,input().split()))

li_set = sorted( list(set(li)))

# print(li_set)
# print(n, li)
lili = [[0 for _ in range(len(li)+1)] for _ in range(len(li_set)+1) ]
# for i in lili:
#     print(i)

for i in range(1, len(li_set)+1):
    for j in range(1, len(li)+1):
        if li[j-1] == li_set[i-1] :
            lili[i][j] = lili[i-1][j-1] + 1
        else:
            up = lili[i-1][j]
            left = lili[i][j-1]
            lili[i][j] = max(up,left)

# for i in lili:
#     print(i)
print(lili[len(lili)-1][len(lili[0])-1])