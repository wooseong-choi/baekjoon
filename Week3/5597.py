li = [0] * 30
for i in range(28):
    x = int(input())
    li[x-1] = x

for i in range(30):
    if li[i] == 0 :
        print(i+1)