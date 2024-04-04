n, m = map(int, input().split())

arr = [ [] for i in range(n+1) ] 


for i in range(1,m+1):
    u , v = map(int, input().split())
    arr[u].append( v )
    arr[v].append( u )


print(arr)

def union (x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root : arr[y] = x_root