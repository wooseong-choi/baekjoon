def big_jongbin(bang:[] ,x:int, y:int) :
    if not (x < y) : return
    for i in range(x, y):
        if i != 0 and i != y:
            if bang[i] != 0 :
                bang[i] = 0
            else :
                if y != i:
                    bang[i] = 0

n = [1 for _ in range(int(input()))]
# print(n)
for _ in range(int(input())) :
    x, y = map(int,input().split())
    big_jongbin(n, x, y)

print(len( list( filter(lambda x: x!=0 ,n) )))
