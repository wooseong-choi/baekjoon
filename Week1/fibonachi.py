n = int(input())
arr = [0,1]
count = 2
while len(arr) <= n:
    arr.append(arr[count-2] + arr[count-1])
    count += 1 
arr.pop(0)
print(arr)




