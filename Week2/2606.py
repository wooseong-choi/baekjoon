n = int(input())
m = int(input())

con_list = [ [] for _ in range(n+1) ]

n_list = [ i for i in range(n+1) ]

for i in range(1,m+1):
    x, y = map(int,input().split())
    con_list[x].append(y)
    con_list[y].append(x)

# print(con_list)
# print(n_list)

def union(child, parent):
    x = find(child) 
    y = find(parent)

    if x == y : return False

    if x <= y : n_list[y] = x
    else : n_list[x] = y

    return True

def find(x):
    if n_list[x] != x:
        n_list[x] = find(n_list[x])
    return n_list[x]

for i,k in enumerate(con_list): 
    for j in k: 
        union(int(i),j)            


# print(n_list.count(1)-1)
cnt = 0
for i in n_list:
    if find(i) == 1: cnt+=1

# print(n_list)


print(cnt-1)