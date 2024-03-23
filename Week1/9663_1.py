#하노이의 탑 규칙 
#1. n번째 원반을 옮기기 위해선 n-1 번째 원반이 다른 기둥에 옮겨져야 한다. 1번째 재귀
#2. n번째 원반을 옮긴 후 n-1 번째 원반이 n번째 원반 위에 옮겨져야 한다. 2번째 재귀
def hanoi(n,start,end):
    midle = 6 - start - end
    
    if n == 1:
        print(start,end)
    else:
        hanoi(n-1,start,midle)
        print( start,end )
        hanoi(n-1,midle, end)
n = int(input())
print(2**n-1)
if(n <= 20):
    hanoi(n,1,3)