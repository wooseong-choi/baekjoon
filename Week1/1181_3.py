#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#중복된 단어 제거
# 버블 정렬 개선 
# 3 단계 셰이커 정렬 
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

left = 0
right = len(arr) -1
last = right
while left < right:
    for j in range(right, left , -1):
        if len(arr[j-1]) > len(arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            
            last = j
        elif len(arr[j-1]) == len(arr[j]):
            temp = []
            temp.extend([arr[j-1],arr[j]])
            #temp.append(arr[j-1])
            #temp.append(arr[j])
            temp.sort()
            arr[j-1],arr[j] = temp[0],temp[1]
            if arr[j-1] == arr[j]:
                arr.pop(j)
            
    left = last    

    for j in range(left, right):
        if len(arr[j]) > len(arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
            last = j
        elif len(arr[j]) == len(arr[j+1]):
            temp = []
            temp.extend([arr[j],arr[j+1]])
            #temp.append(arr[j-1])
            #temp.append(arr[j])
            temp.sort()
            arr[j],arr[j+1] = temp[0],temp[1]
            if arr[j] == arr[j+1]:
                arr.pop(j)
            
    right = last  

print(arr)