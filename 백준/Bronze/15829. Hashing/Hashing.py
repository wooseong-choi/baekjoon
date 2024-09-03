l = int(input())
st = input()
r = 31
m = 1234567891

st_list = list(st)

hasing_num = 0

for idx,i in enumerate(st_list):
    hasing_num += (ord(i)-ord('a')+1) * (r ** idx)

# print(hasing_num)
# print((r**l))

result = hasing_num % m

print(result)

