n, k = map(int, input().split())
que = list(range(1, n + 1))
result = []

import sys
print = sys.stdout.write

temp = 0
# def get(num):
#     return (num + k -1) % len(que)


while len(que) > 0:
    temp =  (temp + k -1) % len(que)
    result.append(que.pop(temp))

#print(f'<{result}>' )
print('<')
for idx, val in enumerate(result):
    if idx == len(result)-1:
        print(str(val))
    else:
        print(str(val)+', ')
    
print('>')