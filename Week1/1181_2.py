#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#중복된 단어 제거
# 버블 정렬 개선 
# 1 단계 : 배열값을 교환하지 않았다면 정렬된것으로 보고 반복문 멈춤. 1,2단계 같이 구현 안되어서 1단계 삭제
# 2단계 마지막으로 배열을 교환한 위치보다 앞쪽은 정렬 완료로 보고 그 이후부터 반복
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

k = 0
while k < len(arr) - 1:
    last = len(arr) - 1
    exchng = 0
    for j in range(len(arr)-1, k , -1):
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
            
    k = last    
print(arr)