import sys

class Heap:
    def __init__(self):
        self.arr = []
        self.output = []

    def heapify_down(self, k , n): # 부모node idx = k # list의 길이 -1 = n
        # 어떤 노드 i 에서 
        # i의 부모 노드 (i-1)//2
        # i의 왼쪽 자식 노드 i*2+1
        # i의 오른쪽 자식 노드 i*2+2
        while 2*k+1 < n:
            L, R = 2*k+1, 2*k+2 # left, right 변수 생성
            if k < n and self.arr[L] > self.arr[k] :
                m = L
            else: 
                m = k 
            if R < n and self.arr[R] > self.arr[m]:
                m = R
            if m != k: 
                self.arr[m], self.arr[k] = self.arr[k], self.arr[m] 
                k = m
            else:
                break

    def heapify_up(self, k): # 어떤 node idx = k
        parent = (k-1)//2 
        while k > 0 and self.arr[parent] < self.arr[k]:
            self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent]
            k = parent
            parent = (k-1)//2

    def insert(self, key) :
        self.arr.append(key)
        self.heapify_up(len(self.arr)-1)

    def delete_max(self):
        if len(self.arr) == 0:
            self.output.append()
            return
        # 가장 마지막 원소와 최상위 노드 원소를 바꿈
        self.arr[0], self.arr[len(self.arr) -1] = self.arr[len(self.arr)-1], self.arr[0] 
        self.output.append(self.arr.pop())
        self.heapify_down(0, len(self.arr))
    
    def print(self):
        if self.output:
            print('\n'.join(map(str, self.output)))

n = int(sys.stdin.readline())
heap = Heap()
for _ in range(n):
    x = int(sys.stdin.readline())
    if x: heap.insert(x)
    else: heap.delete_max()
heap.print()
