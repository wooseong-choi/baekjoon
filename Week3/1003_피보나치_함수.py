t = int(input())

li = [(0,0)] * 41
li[0] = (1,0)
li[1] = (0,1)
li[2] = (1,1)

# li2 = [] * 40

# print(li)

for i in range(3,41):
    # print(i)
    li[i] = (li[i-1][0]+li[i-2][0],li[i-1][1]+li[i-2][1])

# print(li)
for i in range(t):
    n = int(input())
    print( li[n][0], li[n][1])

    