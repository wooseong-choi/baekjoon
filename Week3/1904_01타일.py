n = int(input())

# result = 0

# tile00 = 00
# tile1 = 1
li = []
for i in range(1,n+1):
    # print(li)
    if i == 1:
        li.append((1,i))
    elif i == 2 :
        li.append((2,i))
    else:
        li.append(( i, (li[i-1-1][1]+li[i-2-1][1])%15746 ))


print(li[n-1][1])