n = int(input())
size = list(map(int,input().split()))
t, p = map(int,input().split())

answer_t = 0
answer_p = 0

for i in size:
    if i == 0: continue
    elif i < t :
        answer_t+=1
    else:
        if i%t == 0 :
            answer_t+=(i//t)
        else:
            answer_t+=(i//t)+1

answer_p = str(n//p) +' '+ str(n%p)

print(answer_t)
print(answer_p)

