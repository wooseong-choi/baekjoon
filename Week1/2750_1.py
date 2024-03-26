#퀵 소트
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

def quick(arr:list, pl:int, pr:int):
    pivat = arr[(pl+pr)//2] # 랜덤해도 됨
    pivat_left = pl
    pivat_right = pr 

    if pl >= pr:
        return
    
    while pl <= pr:
        while arr[pl] < pivat : pl += 1
        while arr[pr] > pivat : pr -= 1  
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl +=1
            pr -=1
    quick(arr, pl, pivat_right)
    quick(arr, pivat_left, pr)

quick(arr, 0, len(arr)-1)

for i in arr:
    print(i)