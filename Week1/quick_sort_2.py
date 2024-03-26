import sys
import collections
input = sys.stdin.readline
#print = sys.stdout.write

def quicsort(li, left, right):
    if left >= right:
        return

    pivot = li[(left + right)//2]
    pl = left
    pr = right
    print('pivot',pivot, 'left = ',left,'right = ',right)
    print(f'li[{left}] ~ li[{right}] : ', li)

    while pl <= pr:
        while li[pl] < pivot:
            pl += 1 
        while li[pr] > pivot:
            pr -= 1
        if pl <= pr:
            print( f'pl = {li[pl]}, pr = {li[pr]} as' )
            li[pl], li[pr] = li[pr], li[pl]
            print( f'pl = {li[pl]}, pr = {li[pr]} tobe' )
            pl += 1
            pr -= 1

    quicsort(li, left, pr)
    quicsort(li, pl, right)


if __name__ == '__main':
    num = int(input().rstrip())
    li = collections.deque()

    for i in range(num):
        li.append(int(input().rstrip()))

    quicsort(li, 0, num -1)

    for i in range(num):
        print(str(li[i])+'\n')

