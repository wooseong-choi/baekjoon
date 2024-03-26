import sys

input = sys.stdin.readline

class fixedStack:
    def __init__(self, capacity ) -> None:
        self.ptr = 0 # 현재크기
        self.capacity = capacity # 최대크기
        self.stk = [None] * capacity # 실제 스택 리스트
    
    def push_(self, x:int):
        self.stk[self.ptr] = x
        self.ptr += 1
    def pop_(self):
        if self.ptr == 0 : return -1
        else :
            self.ptr -= 1
            return self.stk[self.ptr]
    
    def size_(self):
        return self.ptr
    
    def empty_(self):
        if self.ptr == 0 :
            return 1
        else: return 0
        

    def top_(self):
        if self.ptr == 0 :
            return -1
        else : 
            return self.stk[self.ptr-1]
        
        

if __name__ == '__main__':
    n = int(input().rstrip())
    fixedStack_1 = fixedStack(n)
    for _ in range(n):    
        command = input().rstrip()
        if command.find('push') != -1:
            pushx = command.split()[1]
            fixedStack_1.push_(int(pushx))
        elif command == 'pop':
            sys.stdout.write( str(fixedStack_1.pop_() )+'\n')
        elif command == 'size' :
            sys.stdout.write(  str(fixedStack_1.size_())+'\n' ) 
        elif command == 'empty' :
            sys.stdout.write( str( fixedStack_1.empty_())+'\n')
        elif command == 'top':
            sys.stdout.write( str(fixedStack_1.top_())+'\n')       