class Node(object):
    def __init__(self, key, data=None):
        print(f'나 트라이 노드! 노드에 값을 저장하지 key = {key}, data = {data}')
        self.key = key
        self.data = data
        self.children = {}

#         노드에는 세가지가 필요합니다.

# 1. key - 값으로 입력될 문자

# 2. data - 문자열의 종료를 알리는 flag. ( True/False로도 구현할 수 있지만, 돌아가는 일이 없게 하기위해 전체 문자열을 저장)

# 3. children - 자식노드를 저장
        

