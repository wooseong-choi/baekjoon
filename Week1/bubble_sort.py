from typing import MutableSequence

def bubble_sort(a:MutableSequence) -> None:
    """버블정렬"""
    n = len(a)
    for i in range(n-1):
        for j in range(n - 1, i ,-1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j-1]

if __name__ == '__main__':
    print('버블정렬 실행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num #원소 수 num 인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)    

    print('오름차순 정렬')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')