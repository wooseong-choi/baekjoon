while True:
    a,b,c = map(int, input().split())
    if a+b+c == 0: break
    if a**2 + b**2 == c**2:
        print('right') 
        continue
    elif a**2 + c**2 == b**2:
        print('right') 
        continue
    elif b**2 + c**2 == a**2:
        print('right') 
        continue
    else :
        print('wrong')
    