t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    m = int(input())
    # print(n, li)

    dp = [0] * (m+1)
    dp[0] = 1

    for i in li:
        # print( i ,end='i = \n')
        for j in range(1, m+1):
            # print( j ,end=' ')
            if j >= i:
                # print( dp[j], dp[j-i])
                dp[j] += dp[j-i]
    print(dp[m])
    # print(dp)