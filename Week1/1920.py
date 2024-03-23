n = int(input())
li = list(map(int, input().split()))
li.sort()
m = int(input())
mli = list(map(int , input().split()))

def binary_search( list, target, start, end ):
    if start > end :
        return None

    middle = (start+end) // 2

    if list[middle] == target:
        return middle
    elif list[middle] > target:
        return binary_search(list, target, start, middle-1)
    else :
        return binary_search(list, target, middle+1, end)

# print(binary_search(li, 1, 0, n-1))

for i in mli:
    w = binary_search(li, i, 0, n-1)
    if w is None: print('0')
    else: print('1')