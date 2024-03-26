n = int(input())
import sys
input = sys.stdin.readline
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class queue:
    def __init__(self, capacity):
        self.no =0 
        self.front =0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def push(self, x):
        if self.no < self.capacity:
            self.que[self.rear] = x
            self.no += 1
            self.rear +=1    
            if self.rear == self.capacity:
                self.rear = 0
        
    def pop (self):
        x = self.que[self.front]
        if x is None : return -1
        self.que[self.front] = None
        self.front +=1
        self.no -=1
        if self.front == self.capacity:
            self.front = 0
        return x

    def size(self):
        return self.no
    
    def empty(self):
        return 1 if self.no <= 0 else 0
    
    def getFront(self):
        return self.que[self.front] if self.no > 0 else -1
    
    def getBack(self):
        return self.que[(self.rear - 1 + self.capacity) % self.capacity] if self.no > 0 else -1
que_ = queue(n)
for _ in range(n):

    command = input().rstrip()
    if command.find('push ') != -1:
        que_.push(command.split()[1])
    elif command == 'pop':
        print(que_.pop())
    elif command == 'size':
        print(que_.size())
    elif command == 'empty':
        print(que_.empty())
    elif command == 'front':
        print(que_.getFront())
    elif command == 'back':
        print(que_.getBack())
