t = int(input())
sco = list(map(int, input().split()))

high = max(sco)
sum = 0
for i in range(t):
    sum += sco[i]/high*100

print(sum/t)