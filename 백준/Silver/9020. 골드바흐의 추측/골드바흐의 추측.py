t = int(input())

"""에라토스테네스의 체 구하기"""
n = 10000
a = [False,False] + [True]*(n)
primes=[]

for i in range(2, n):
    if a[i]:
        primes.append(i)
        """배수들 제거"""
        for j in range(2*i, n, i):
            a[j] = False
# print(primes)

for i in range(t):
    num = int(input())
    small = 0
    big = 0
    for j in primes:
        if j >= num/2:
            for k in primes:
                if k + j == num:
                    if big == 0:
                        small = k
                        big = j
                    break
                if big > 0 :
                    break
        if big > 0 :
            break
    print(small, big)

