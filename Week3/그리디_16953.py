n, m = map(int, input().split())

def add1(x):
    return int(str(x)+'1')

def times2(x):
    return x*2


import collections
#큐 없이 풀려면 어떻게 해야 할까
que = collections.deque()
que.append((n,1))

def bfs():
    while que:
        val, cnt = que.popleft()

        # print(val, cnt)
        if val == m :
            return print(cnt)
        

        
        if (val*10+1) <= m: que.append((add1(val),cnt+1))
        if (val*2) <= m :que.append((times2(val),cnt+1))
    
    print(-1)

bfs()

# 난 이거 못품
