for i in range(int(input())):
    s = input().split()
    result = ''
    for j in s:
        if result == '':
            result += j[::-1]            
        else :
            result += ' '+j[::-1]
    print(result)