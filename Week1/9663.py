# 난 이걸 풀지 못했다
n = int(input())
def goHanoi(num,start,to,via):
    if num == 1:
        print(start, to, end=' \n' )
    else:
        goHanoi(num-1,start, via,to)
        print( start,to, end=' \n' )
        goHanoi(num-1, via,to,start)
def hanoiCnt(num):
    return 2**num-1
print(hanoiCnt(n))
if(n <= 20):
    goHanoi(n,1,3,2)