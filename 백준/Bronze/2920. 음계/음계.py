# a = list(map(int, input().split()))
# li = []
# for idx,i in enumerate(a):
#     if idx > 0:
#         li.append(a[idx-1] - a[idx])
# sum = 0
# for i in li:
#     sum += i

# if sum == 7:
#     print('ascending')
# elif sum == -7:
#     print('descending')
# else:
#     print('mixed')

a = input()
if a == '1 2 3 4 5 6 7 8':
    print('ascending')
elif a == '8 7 6 5 4 3 2 1':    
    print('descending')
else:
    print('mixed')