from typing import MutableSequence

def shaker_sort(a:MutableSequence) -> None:
    """버블정렬"""
    n = len(a)
    left =0
    right = n -1
    last = right
    while left < right:
        for j in range(right, left ,-1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1] , a[j]
                last = j
        right = last 


if __name__ == '__main__':
    print('쉐이커 정렬 실행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num #원소 수 num 인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)    

    print('오름차순 정렬')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')