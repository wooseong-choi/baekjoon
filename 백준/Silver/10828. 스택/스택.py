import sys

stack = []

def push( x ):
    stack.append(x)

def pop():
    if len(stack) == 0 :
        return -1
    else:
        result = stack[-1]
        stack.pop()
        return result

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0

def top():
    return -1 if len(stack) == 0 else stack[-1]

for i in range(int(sys.stdin.readline())):
    com = sys.stdin.readline().strip()
    scom = com.split()
    if scom[0] == 'push':
        push(scom[1])
    elif com == 'top':
        sys.stdout.write(str(top())+'\n')
    elif com == 'size':
        sys.stdout.write(str(size())+'\n')
    elif com == 'empty':
        sys.stdout.write(str(empty())+'\n')
    elif com == 'pop':
        sys.stdout.write(str(pop())+'\n')
