r = int(input())
c = 0
l = list(input().split())
for i in l:
    count = 0

    for j in range(2,int(i)+1):
        if int(i)%j == 0:
            count+=1

    if count == 1:
        c+=1
print(c)

# 더 빨리할수 있는 방법이 없을까