n = int(input())
temp = list(map(int, input().split()))
arr = []
# for idx,i in enumerate(temp):
#     arr.append(((idx+1),i))

temp.sort()
# print(temp)

if len(temp) % 2 == 1 : 
    arr.append(temp[-1])
    temp = temp[:-1]

for i in range(len(temp)//2):
    arr.append(temp[i] + temp[len(temp)-1])
    temp.pop()

print(max(arr))