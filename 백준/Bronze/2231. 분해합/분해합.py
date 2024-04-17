n = int(input())
j = True
for i in range(1,1000000):
    sum = 0
    for s in str(i):
        sum += int(s)
    if (sum + i) == n:
        print(i)
        j = False
        break
if j:
    print(0)