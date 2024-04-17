# t = int (input())
# for i in range(t):
#     h,w,n = map(int, input().split())
#     roomW = 1
#     if n//h == 0 :
#         roomH = n%h
#     else:
#         roomW += n//h
#         roomH = n%h
#     print( roomH,roomW )
#     print(str(roomH) + ('0'+str(roomW)[-2:]))

a = []
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if n > h:
        if n%h == 0:
            if n//h +1 < 10:
                a.append(f"{h}{('0'+str(n//h))[-2:]}")
            else:
                a.append(f"{h}{('0'+str(n//h))[-2:]}")
        else:
            if n//h +1 < 10:
                a.append(f"{n%h}{('0'+str(n//h+1))[-2:]}")
            else:
                a.append(f"{n%h}{('0'+str(n//h+1))[-2:]}")
    elif n == h:
        a.append(f"{n}01")
    else:
        a.append(f"{n%h}01")
for i in range(t):
    print(a[i])