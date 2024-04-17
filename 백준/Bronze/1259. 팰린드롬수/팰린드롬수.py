while (True):
    s = input()
    if s == '0':
        break
    
    
    boolean = True

    # 홀수의 경우
    if len(s)%2 == 1:
        li = list(s[0:len(s)//2])
        s = s[len(s)//2+1:]
        # print(li)
        # print(s)
        for i in s:
           if i != li.pop():
                print('no')
                boolean = False
                break
        
        if len(li) == 0 and boolean:
            print('yes')
               
    # 짝수의 경우
    else:
        li = list(s[0:len(s)//2])
        s = s[len(s)//2:]
        # print(li)
        # print(s)
        for i in s:
           if i != li.pop():
                print('no')
                boolean = False
                break        
        if len(li) == 0 and boolean:
            print('yes')