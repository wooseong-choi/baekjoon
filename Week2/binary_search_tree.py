from __future__ import annotations
from typing import Any, Type
class Node:
    """이진 검색 트리의 노드"""
    def __init__ (self, key, value, left = None, right = None):
        self.key = key #키
        self.value = value #발 
        self.left = left #왼쪽포인터
        self.right = right #오른쪽 포인터

class BinarySearchtree:
    """이진 검색 트리"""
    def __init__(self):
        self.root = None
    
    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else :
                p = p.right
    
    def add(self, key, value) -> bool:

        def add_node(node, key, value)-> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value 인 노드를 삽입"""

            if key == node.key:
                return False # key가 이미 이진 트리에 존재하므로 삽입할수 없음 
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None,None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
                
            return True
        
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root, key, value)
        
    def remove( self, key) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root # 스캔중인 노드
        parent = None # 스캔중인 노드의 부모 노드
        is_left_child = True # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None: # 더 이상 진행할수 없으면
                return False # 그 키는 존재하지 않음
        
            if key == p.key: # 키가 같으면
                break # 검색 성공
            else:
                parent = p # 가지를 내려가지 전에 부모를 설정
                if key < p.key: # 찾는 키값이 부모의 키보다 작으면
                    is_left_child = True # 왼쪽 노드에서 찾는다
                    p = p.left
                else:
                    is_left_child = False 
                    p = p.right
        
        if p.left is None:  # p에 왼쪽 자식이 없으면
            if p is self.root : 
                self.root = p.right
            elif is_left_child:
                parent.left = p.right # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None: # 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        
        else :
            parent = p
            left = p.left # 서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None: # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key # left의 키를 p로 이동
            p.value = left.value # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left # left를 삭제
            else:
                parent.right = left.left # left를 삭제
        
        return True

    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""

        def print_subtree(node:Node):
            """node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left) # 왼쪽 서브트리를 오름차순으로
                print(f'{node.key}  {node.value}') # node 출력
                print_subtree(node.right) # 오른쪽 서브트리 오름차순 출력

        print_subtree(self.root)
    
    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key