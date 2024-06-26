from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """단순 선택 정렬"""
    n = len(a)
    for i in range(n -1 ):
        min = i # 정렬할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n ):
            if a[j] < a [min]:
                min =j

        a[i], a[min] = a[min], a[i]        

if __name__ == '__main__':
    print('선택 정렬 실행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num #원소 수 num 인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    selection_sort(x)    

    print('오름차순 정렬')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')        