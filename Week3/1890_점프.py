n = int(input())

li = [[0] for i in range(n+1)] 



for i in range(1,n+1):
    li[i] = list(map(int, input().split()))
    li[i].insert(0,0)
# print(li)   

from collections import deque 

que = deque()

que.append(((1,1),li[1][1]))

cnt = 0
# print(que)

while que:
    key,val = que.popleft()
    
    # if val == 0 : 

    # print(key,val)

    if val > n-key[0] or val == 0:
        pass
    else:
        que.append( ( (key[0]+val, key[1]),li[key[0]+val][key[1]] ) )
        if li[key[0]+val][key[1]] == 0 :
            cnt += 1

    if val > n-key[1] or val == 0:
        pass
    else:
        que.append( ( (key[0], key[1]+val),li[key[0]][key[1]+val] ) )
        if li[key[0]][key[1]+val] == 0 :
            cnt += 1

print(cnt)