n = int(input())
temp = map(int, input().split())
arr = []
for idx,i in enumerate(temp):
    arr.append(((idx+1),i))

print(arr)

