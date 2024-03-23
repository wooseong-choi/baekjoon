#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#중복된 단어 제거
# 버블 정렬로는 실패하였음
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(len(arr)):
    for j in range(len(arr)-1, i , -1):
        if len(arr[j-1]) > len(arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
        elif len(arr[j-1]) == len(arr[j]):
            temp = []
            temp.extend([arr[j-1],arr[j]])
            #temp.append(arr[j-1])
            #temp.append(arr[j])
            temp.sort()
            arr[j-1],arr[j] = temp[0],temp[1]
            if arr[j-1] == arr[j]:
                arr.pop(j)
print(arr)