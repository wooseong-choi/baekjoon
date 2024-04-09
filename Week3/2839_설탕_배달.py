n = int(input())

# 설탕의 무게 n
# 상근이가 가진 봉지 용량 3, 5
# 상근이는 봉지를 무한히 가지고 있다

if n < 5 and n != 3 :
    print(-1)
    exit()

if n == 3 :
    print(1)
    exit()

from collections import deque
queue = deque()

def i_like_sugar( weight, cnt):
    
    queue.append((weight,cnt))
    while queue:
        weight_temp,cnt_temp = queue.popleft() 
       
        if weight_temp%5 == 0 :
            cnt_temp += weight_temp//5
            return print(cnt_temp)
        else:
            weight_temp -= 3
            cnt_temp += 1
            if weight_temp == 0 :
                return print(cnt_temp)
        # print(weight_temp)
        if weight_temp < 3 :
            return print(-1)
        queue.append((weight_temp,cnt_temp))

i_like_sugar(n,0)


# 설탕 배달
# total = int(input())
# group = [3,5]
# dp = [0] * (total+1)
# for g in group:
#   for i in range(g,total+1):
#     if i - g == 0:
#       dp[i] +=1
#     if dp[i-g] >= 1:
#       dp[i] = dp[i-g]+ 1
# if dp[-1] == 0:
#   print(-1)
# else:
#   print(dp[-1])