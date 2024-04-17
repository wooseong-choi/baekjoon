n = int(input())

li = []

sum = 0

temp_idx = 0
past_step_idx = -1

li.append(0)
for i in range(n):
    li.append(int(input()))

for idx,i in enumerate(li):
    # if idx == 0 : 
        # sum = li[idx+1]
        # temp_idx = idx + 1
        
    if temp_idx <= idx:
        # 마지막 계단만 남은 경우
        if len(li)-1 == idx+1: 
            sum += li[idx+1]
            temp_idx = idx+1
            past_step_idx = idx
            break
        
        # 이전에 밡은 계단이 바로 한칸 아래의 계단인 경우
        if past_step_idx == idx-1 and past_step_idx > -1:
            if len(li)-1 == idx+2: 
                sum += li[idx+2]
                temp_idx = idx+2
                past_step_idx = idx
                break 
            
            if len(li)-1 >= idx+2:
                l1 = li[idx+1]
                l2 = li[idx+2]
                if l1 > l2:
                    temp_idx = idx+1
                else: 
                    temp_idx = idx+2

                past_step_idx = idx
                sum += max( li[idx+1], li[idx+2] )

        # 풀다보니 꼬였는데 잘 모르겠습니다
        else :
            if len(li)-1 >= idx+3:
                l1 = li[idx+1]
                l2 = li[idx+2]
                l3 = li[idx+3]
                l4 = li[idx+4]

                if l1 + l2 > l3 :
                    temp_idx = idx+1
                    sum += li[idx+1]    
                elif l1 + l2 < l3:
                    temp_idx = idx+2
                    sum += li[idx+2]
                else:
                    temp_idx = idx+2
                    sum += li[idx+2]



                # temp_idx = idx+1
                past_step_idx = idx
                # sum += li[idx+1]
                # l1 = li[idx+1]
                # l2 = li[idx+2]
                # if l1 > l2:
                #     temp_idx = idx+1
                # else: 
                #     temp_idx = idx+2
                
                # past_step_idx = idx
                # sum += max( li[idx+1], li[idx+2] )
            

    # print('sumsusmsusm',sum)

print(sum)

# 정답코드 나중에 풀이 할 것

# import sys
# input = sys.stdin.readline
# n = int(input())
# stair = [int(input()) for _ in range(n)]


# def up(stair):
#     m = len(stair)
#     dp = [0] * (m)
#     if m == 1:
#         return stair[0]
#     elif m == 2:
#         return sum(stair)
#     dp[0] = stair[0]
#     dp[1] = stair[0] + stair[1]
#     dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
#     for i in range(3,n):
#         dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
#     return dp[-1]
# print(up(stair))