n = int(input())
s = input()
sum = 0
add_arr = ''
for i in range(n):
    if s[i].isdecimal():
        add_arr += s[i]
    else :
        if add_arr != '':
            sum += int(add_arr)
            add_arr = ''
if add_arr != '':
    sum += int(add_arr)

print(sum)