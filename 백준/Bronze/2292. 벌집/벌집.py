n = int(input())

cnt = 1
maxblock = 1

while n > maxblock:
    maxblock += 6 * cnt
    cnt+=1

print(cnt)