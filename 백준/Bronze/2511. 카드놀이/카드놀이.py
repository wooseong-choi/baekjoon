a = list(map(int, input().split()))
b = list(map(int, input().split()))
record = []
d_cnt = 0
for i in range(len(a)):
    if a[i] == b[i]:
        record.append('D')
        d_cnt+=1
    elif a[i] > b[i] :
        record.append('A')
    elif a[i] < b[i] :
        record.append('B')

if d_cnt == len(a):
    print(len(a), len(b))
    print('D')
else:
    a_cost = 0
    b_cost = 0
    isAwin = None
    for i in record:
        if i == 'A': 
            a_cost+=3
            isAwin = True
        elif i == 'B': 
            b_cost+=3
            isAwin = False        
        elif i == 'D' : 
            a_cost+=1
            b_cost+=1
    print(a_cost,b_cost)    
    if a_cost != b_cost:
        print('A' if a_cost > b_cost else 'B')
    else:
        print('A' if isAwin else 'B')