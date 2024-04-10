import sys

n = int(input())

li = [ 0 for _ in range(n+1) ]

temp = []

for i in range(1,n+1):
    s, e = map(int, sys.stdin.readline().split())
    temp.append((s,e))

temp.sort(key=lambda x : (x[1],x[0])) # 먼저 끝나면서 먼저 시작하는 순으로 정렬

result = []

for i in range(len(temp)):
    k, v = temp[i]
    if len(result) == 0 :
        result.append((k,v))
    else:
        tf = True

        res_srt, res_end = result[len(result)-1]
        if k < res_end :
            tf = False        
        if tf :
            result.append((k,v))




print(len(result))
