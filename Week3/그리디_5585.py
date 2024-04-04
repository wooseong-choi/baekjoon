n = int(input())

m = 1000-n

cnt = 0
while m > 0:
    if m%500 == 0 :
        cnt += m//500
        m = m%500
        
    else : 
        cnt += m//500
        m = m%500
        
    if m&100 == 0:
        cnt += m//100
        m = m%100
        
    else:
        cnt += m//100
        m = m%100

    if m%50 == 0:
        cnt += m//50
        m = m%50
        
    else:
        cnt += m//50
        m = m%50

    if m%10 == 0:
        cnt += m//10
        m = m%10
        
    else:
        cnt += m//10
        m = m%10

    if m%5 == 0:
        cnt += m//5
        m = m%5
        
    else:
        cnt += m//5
        m = m%5

    if m%1 == 0:
        cnt += m//1
        m = m%1
        
    else:
        cnt += m//1
        m = m%1

print(cnt)