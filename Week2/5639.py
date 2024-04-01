import sys
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        arr.append(int(input()))
    except: break

def post_order(array):
    if len(array) == 0 : return
    arr_left = []
    arr_right = []

    # root = array[0]
    # for i in range(1,len(array)):
    #     if array[i] < root:
    #         arr_left.append(array[i])
    #     else:
    #         arr_right.append(array[i])
    # 위의 코드 개량
    # 첫번째 값을 루트 노드로 설정
    root = array[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(array)):
        if array[i] > root:
            arr_left = array[1:i]
            arr_right = array[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        arr_left = array[1:]

    post_order(arr_left)
    post_order(arr_right)
    print(root)


post_order(arr)