n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
remain = sum(a)
meter = 0
for ai in a:
    remain_ai = ai
    for bj in range(meter, len(b)):
        if remain_ai >= b[bj]:
            remain_ai-=b[bj]
            remain-=b[bj]
            meter+=1
        else:
            break

print(remain)