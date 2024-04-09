t = int(input())

li = []
li.append(0)
li.append(1)
li.append(2)
li.append(4)

for i in range(4,11):
    li.append(li[i-1]+li[i-2]+li[i-3])


     

# print( li )

for i in range(t):
    print(li[int(input())])