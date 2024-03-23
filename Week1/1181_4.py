#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#중복된 단어 제거
# 내부 메소드
n = int(input())
arr= []
for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort()
arr.sort(key=len)

for i in arr:
    print (i)
