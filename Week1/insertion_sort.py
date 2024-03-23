from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n ):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j - 1]
            j -= 1 
        a[j] = tmp

if __name__ == '__main__':
    print('선택 삽입 실행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num #원소 수 num 인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)    

    print('오름차순 정렬')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')        