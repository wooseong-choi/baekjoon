h, m = map(int, input().split())
if h == 0 : h = 24
# if m == 0 : m = 60

if m < 45 :
    h -=1
    m +=60

m -= 45

if h == 24 :
    h = 0
if m == 60 :
    m = 0
print(h,m)