import sys
print = sys.stdout.write
input = sys.stdin.readline

def quick_sort(start, end):
    if start >= end :
        return

    pivot = r[(start + end) // 2]
    pl = start
    pr = end 


    while pl <= pr:
        while r[pl] < pivot: pl +=1
        while r[pr] > pivot: pr -=1
        if pl <= pr :
            r[pl], r[pr] = r[pr], r[pl]
            pl +=1
            pr -=1
        print(f' pl = {pl} pr = {pr}')    
    quick_sort(start, pr)
    quick_sort(pl, end)

    

n = int(input())
r = []
for _ in range(n):
   r.append(int(input()))

quick_sort(0,len(r)-1)

for i in r:
    print(str(i)+"\n") 


