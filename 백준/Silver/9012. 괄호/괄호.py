for i in range(int(input())):
    s = input()
    opencnt = 0
    closecnt = 0
    no = False
    if len(s)%2 == 0 :
        for index,j in enumerate(s):
            if (j == '('):
                opencnt += 1
                if opencnt > len(s)//2:
                    no = True
            if (j == ')'):
                closecnt += 1
                if opencnt < closecnt:
                    no = True
                if index == 0 :
                    no = True
        print('NO' if no else 'YES')
    else:
        print('NO')