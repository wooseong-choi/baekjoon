s = input()
li = []
result = []
# 알파벳의 아스키 코드에 - 96을 하면 알파벳을 숫자로 변환한 값을 얻을 수 있다.
for i in range(97,123):
    li.append(chr(i))

# print(li)

for zIdx,z in enumerate(li):
    for idx,i in enumerate(s):
        if s[idx] == z:
            # print(s[idx], idx)
            if str(type(li[zIdx])) != "<class 'int'>":
                li[zIdx] = idx
    
for idx,z in enumerate(li):
    # print(str(type(z)), z)
    if str(type(z)) != "<class 'int'>" :
        if 96 < ord(z) < 123:
            li[idx] = -1

for i in li : print(i,end=' ')