def fact(n):
    if n == 0 :
        return 1
    return n*fact(n-1)
print(fact(int(input())))


r = 1
for i in range(1,int(input())+1):
    r*=i
print(r)
