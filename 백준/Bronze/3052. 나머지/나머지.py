li = []

cnt = 1

for i in range(10):
    li.append(int(input())%42)

li.sort()

for i in range(10):
    if i > 0:
        if li[i] != li[i-1]:
            cnt +=1
print(cnt)