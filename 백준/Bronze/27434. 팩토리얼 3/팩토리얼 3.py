n = int(input())
if n == 0 : print(1)

else :
    r = 1
    for i in range(n, 1, -1):
        r*=i 
    
    print(r)