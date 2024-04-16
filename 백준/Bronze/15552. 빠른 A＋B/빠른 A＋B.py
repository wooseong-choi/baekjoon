import sys
t = int(input())
for _ in range(t):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(a+b)+'\n' )