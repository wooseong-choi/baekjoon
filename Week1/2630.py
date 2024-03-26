# 답지 보고 품


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

lli = []

def devide_conquest(  y, x, n):
    
    color = arr[y][x]

    for i in range( y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != color :
                devide_conquest( y, x, n//2) # 1사분면
                devide_conquest( y, x+n//2, n//2) # 2사분면
                devide_conquest( y+n//2, x, n//2) # 3사분면
                devide_conquest( y+n//2, x+n//2, n//2) # 4사분면  
                return
    if color == 0 :
        lli.append(0)
    else : 
        lli.append(1)

devide_conquest(0,0,len(arr))            
print(lli.count(0))
print(lli.count(1))
