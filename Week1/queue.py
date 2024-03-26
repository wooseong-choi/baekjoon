n = int(input())
queue = [None] * n

class FixedQueue:

    class Empty(Exception):
        """예외처리"""
        pass

    class Full( Exception):
        """가득차있을때 예외 처리"""
        pass

    def __init__(self, capacity):
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 앞쪽 큐 번호
        self.near = 0 # 뒷쪽 큐 번호 
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐 본체
    
    def __len__(self) :
        """큐에있는 모든 개수를 반환"""
        return self.no
    
    def is_empty(self) :
        return self.no <= 0
    
    def is_full(self):
        return self.no >= self.capacity
    
    def enque(self, val):
        if self.is_full():
            raise FixedQueue.Full 
        self.que[self.near]
        self.near+=1
        self.no += 1
        if self.near == self.capacity:
            self.rear = 0
            
    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty 
        
        x = self.que.pop(self.front)
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return 0
    
    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self , value):
        c= 0
        for i in range(self.no):
            idx = (i + self.front)% self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value):
        return self.count(value)
    
    def clear(self) :
        self.no = self.front = self.rear = 0
    
    def dump(self):
        if self.is_empty():
            print('큐가 비었습니다.')
        else :
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()
            
    