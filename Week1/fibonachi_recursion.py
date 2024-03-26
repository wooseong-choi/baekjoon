arr = []
arr_n = []

def fibonachi (num) :
    if arr_n[num] == 1:
        return arr.append(1)
    arr.append(fibonachi(arr_n[num-2])+fibonachi ( arr_n[num-1] ) )

n = int(input())
for i in range(n):
    arr_n.append(i)

fibonachi(n)
print(arr)