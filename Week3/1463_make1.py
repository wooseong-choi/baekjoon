n = int(input())
cnt = 0
def divide3(x,check:bool=None):
    global cnt
    if check:
        if x > 2 and x%3 == 0:
            return True
        else: return False
    else:
        cnt += 1
        return x//3

def divide2(x, check:bool=None):
    global cnt
    if check:
        if x > 1 and x%2 == 0:
            return True
        else: return False
    else:
        cnt += 1
        return x//2

def minus1(x:int):
    global cnt
    x-=1
    cnt += 1
    return x

if n == 1 : 
    print(0) 
    exit()

from collections import deque

queue = deque()
queue.append((n,0))

li = []

while queue:
    n_temp, cnt_temp = queue.popleft()
    print(n_temp, cnt_temp)
    if n_temp <= 0 : continue


    if n_temp == 1:
        li.append(cnt_temp)
        #break

    if divide3(n_temp,True) and divide2(n_temp,True):
        n_temp_1 = divide3(n_temp)
        n_temp_2 = divide2(n_temp)
        queue.append((min(n_temp_1,n_temp_2),cnt_temp+1))
    elif divide3(n_temp,True):
        n_temp = divide3(n_temp)
        queue.append((n_temp,cnt_temp+1))
    elif divide2(n_temp,True):
        n_temp = divide2(n_temp)
        queue.append((n_temp,cnt_temp+1))
    else: 
        n_temp = minus1(n_temp)
        queue.append((n_temp,cnt_temp+1))

print(li)
# print(min(li))
    
# 1로 만들기
# N = int(input())
# dp = [0] * (N+1)
# for i in range(2,N+1):
#   if i % 3 == 0 and i % 2 == 0:
#     dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
#   elif i % 3 == 0:
#     dp[i] = min(dp[i//3] + 1, dp[i-1]+ 1)
#   elif i % 2 == 0:
#     dp[i] =min(dp[i//2] + 1, dp[i-1]+ 1)
#   else:
#     dp[i] = dp[i-1] + 1
# print(dp[-1])