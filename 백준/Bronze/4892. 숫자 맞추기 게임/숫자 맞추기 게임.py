cnt = 1
def cacul(n0):
    global cnt
    n1 = n0*3
    odd = False if n1%2 == 0 else True
    n2 = (n1+1)/2 if odd else n1/2
    n3 = n2*3
    n4 = n3//9
    print(f"{cnt}. {'odd' if odd else 'even'} {n4}".rstrip('0').rstrip('.'))
    cnt+=1

while True:
    n = int(input())
    if n == 0 : break
    cacul(n)