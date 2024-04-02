def union(parent: list ,x:int, y:int):
    x = find(parent,x) # x의 부모노드 찾기
    y = find(parent,y) # y의 부모노드 찾기

    # 이미 같은 그래프에 속해있을 때 false 반환
    if x == y : return False

    if x <= y : parent[y] = x
    else : parent[x] = y

    return True

def find (parent:list,x:int):
    if parent[x] == x : return x
    return find(parent,parent[x])

if __name__ == '__main__':

    n = 5
    parent = [ _ for _ in range(n+1)]

    union(parent,1,2)
    print(parent)
    
    union(parent,3,4)
    print(parent)
    union(parent,3,5)
    print(parent)

    print( find(parent,2))
    print( find(parent,4))

    union(parent, 2,4)
    print(parent)
    print(find(parent,4))