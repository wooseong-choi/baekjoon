# 체인법으로 해시함수 구하기
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key:Any,value:Any, next:Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next 

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self, capacity : int ) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [None] * self.capacity 
    
    def hash_value(self, key: Any) -> int :
        """해시값 만들기"""
        if isinstance(key,int):
            return key % self.capacity
        return(int(hashlib.sha512(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key:Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash_key = self.hash_value(key)
        p = self.table[hash_key]

        while p is not None:
            if p.key == key:
                return p.value 
            p = p.next
        
        return None
    
    def add(self, key:Any , value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash_key = self.hash_value(key) # 추가하는 key의 해쉬값
        p = self.table[hash_key]

        while p is not None:
            if p.key == key:
                return False
            p = p.next
        
        temp = Node(key, value, self.table[hash_key])
        self.table[hash_key] = temp
        return True

    def remove(self, key: Any) -> bool :
        hash_key = self.hash_value(key)
        p = self.table[hash_key]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash_key] = p.next
                else :
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()
