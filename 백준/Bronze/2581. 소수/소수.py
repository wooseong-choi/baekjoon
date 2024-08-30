def eratosthenes_sieve(m, n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [i for i in range(max(2, m), n+1) if sieve[i]]

m = int(input())
n = int(input())

primes = eratosthenes_sieve(m, n)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))