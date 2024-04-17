n = int(input())
for i in range(1,n+1):
    star = '*'*i
    space = ' '*(n-i)
    print(space,end='')
    print(star)
