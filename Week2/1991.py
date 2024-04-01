#트리 구조를 나타내기 위한 Node 클래스 생성
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
# 전위순회
def preOrder( node):
    print(node.value,end='')
    if node.left != '.':preOrder( tree[node.left] )
    if node.right != '.':preOrder(tree[node.right])
#중위순회
def middleOrder(node):
    if node.left != '.':middleOrder(tree[node.left])
    print(node.value,end='')
    if node.right != '.':middleOrder(tree[node.right])
#후위순회
def suffOrder(node):
    if node.left != '.': suffOrder(tree[node.left])
    if node.right != '.': suffOrder(tree[node.right])
    print(node.value,end='')

n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())
#트리 구조를 편하게 사용하기 위해 딕셔너리를 사용한다
tree = {}
for value, left, right in inputs:
    tree[value] = Node(value,left, right)
preOrder(tree['A'])
print()
middleOrder(tree['A'])
print()
suffOrder(tree['A'])
