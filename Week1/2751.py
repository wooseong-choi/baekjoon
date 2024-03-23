import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))
r.sort()
for i in r:
    print(str(i)+"\n") 


