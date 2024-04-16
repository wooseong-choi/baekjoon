s = input().lower()

if len(s) > 1000000:
    exit()

sets = set(s)

li = [ 0 for _ in range(len(sets)) ]
result = [ '' for _ in range(len(sets)) ]

cnt = 0
temp = cnt
for i in  range(len(sets)):
    ss = sets.pop()
    cnt = s.count(ss)
    
    li[i] = cnt
    result[i] = ss
    # if cnt == temp : 
    #     result = '?'
    #     break
    
    # if temp < cnt:
    #     temp = cnt
    #     maxlen = cnt
    #     result = ss
    # else :
    #     temp = temp

if li.count(max(li)) > 1:
    print('?')
else :
    for i in range(len(li)):
        if li[i] == max(li):
            print(result[i].upper())
            break
# print(result.upper())