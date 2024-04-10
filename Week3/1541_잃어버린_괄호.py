n = input()

li = []
temp = 0
li = n.split('-')
# print(li)
# for idx, val in enumerate(n):
#     pass
    # if val == '-' or val == '+':
    #     li.append( str(int(n[temp:idx])) ) 
    #     li.append(val)
    #     temp = idx+1
    # if idx == len(n)-1 : 
    #     li.append(str(int(n[temp:])))

for idx,i in enumerate(li):
    if i.find('+') == -1:
        li[idx] = str(int(i))
    else :
        temp = 0
        for jdx, j in enumerate(i.split('+')):
            temp += int(j)
        li[idx] = str(temp)


print(eval('-'.join(li)))

# for idx, val in enumerate(li):
#     pass

# print(li)

# print(eval(''.join(li)))