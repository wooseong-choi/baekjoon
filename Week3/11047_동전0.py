n, k = map(int,input().split())

coins = [0] * (n+1) 

for i in range(1,n+1):
    coins[-1*i] = int(input())

# print(coins)

cnt = 0
temp_k = k
for i,coin in enumerate(coins):
    if i == 0 : continue
    if temp_k == 0 :
        break
    if coin == temp_k :
        cnt += temp_k//coin
        temp_k = temp_k%coin
        # print(1)
        # print(i, coin)
        # continue
        break
    elif coin < temp_k:
        temp_cnt = temp_k//coin
        temp_k = temp_k%coin
        cnt += temp_cnt
        # print(i, coin)
    # print(i)
    
   
print(cnt)