sum = 1
for i in range(3):
    sum *= int(input())

sum = f'{sum}'
# print(sum)
for i in range(10):
    print(sum.count(str(i)))