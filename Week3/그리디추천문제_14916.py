n = int(input())

binary = 0
quinary = 0

# quinary = n//5 
# n = n%5
# binary = n//2
# n = n%2

# for i in n
minus = False
while True:
    if n == 1 : 
        minus = True 
        break

    if n%5 > 0:
        n-=2
        binary+=1
    elif n%5 == 0:
        quinary = n//5    
        break
    else:
        minus = True
        break


if minus :
    print(-1)
else : 
    print(quinary+binary)
