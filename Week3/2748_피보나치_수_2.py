n = int(input())

# i = 0
# result = 0
# temp1 = 0
# temp2 = 0
# while i <= n:
#     if i < 2:
#         result += i
#         temp1 = 0
#         temp2 = i
#     else :
#         result = temp1+temp2   
#         temp1 = temp2
#         temp2 = result   
#     i+=1

li = []

for i in range(n+1):
    if i < 2:
        li.append(i)
    else:
        li.append(li[i-1]+li[i-2])

print(li[n])