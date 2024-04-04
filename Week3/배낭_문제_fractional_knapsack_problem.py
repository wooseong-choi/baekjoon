n = int(input()) # 배낭에 담을 수있는 무게
m = int(input()) # 곡식 배열의 크기

m_arr = [(0,0)] * (m+1)
for i in range(1, len(m_arr)):
    w, p = map(int, input().split())
    m_arr[i] = (p,w)



m_arr.sort(key=lambda x: x[0] ,reverse=True)
# print(m_arr)
all_weight = 0
weight = [] 
price = []
for i in range(len(m_arr)-1):
    p, w = m_arr[i]
    all_weight += w
    # print('w ',w)
    weight.append(w)
    price.append(p)

    if all_weight >= n:
        # print(weight[i])
        # print(weight[i]-n)
        weight[i] -= (all_weight - n)
        all_weight = n
        break
    
for i,v in enumerate(weight):
    print( i+1,' ', v , ' : ' ,price[i])



