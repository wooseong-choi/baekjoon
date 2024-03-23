c = int(input())
for _ in range(c):
    a,b = map(str, input().split())
    result = ''
    for j in b:
        for i in range(int(a)):
            result += j
    print(result)

# 더 빠르게
#t=int(input())
#for _ in range(t):
#    n,s=input().split()
#    for i in s:
#        print(i*int(n),end="")
#    print()