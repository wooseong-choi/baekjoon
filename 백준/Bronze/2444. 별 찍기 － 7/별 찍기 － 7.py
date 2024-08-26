n = int(input())
 
def byeol(num:int):
    for i in range(num):
        r = ''
        for j in range((num-1)-i):
            r += ' '
        for k in range(i*2):
            r += '*'
        r+='*'
        print(r)
    for i in range(num-1, 0, -1):
        r = ''
        for j in range((num-i)):
            r+= ' '
        for k in range((i-1)*2):
            r+= '*'
        r+='*'
        print(r)
byeol(n)