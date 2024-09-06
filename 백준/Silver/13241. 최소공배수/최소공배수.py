def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1, num2 = map(int, input().split())
result = lcm(num1, num2)
print(result)