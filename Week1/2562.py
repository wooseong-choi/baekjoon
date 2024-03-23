a = []
for _ in range(9):
    a.append(int(input()))
max = 0
position = 0
for i,v in enumerate(a):
    if v > max:
        max = v
        position = i+1
print(max)
print(position)


#a=[int(input()) for i in range(9)]
#print(max(a))
#print(a.index(max(a))+1)