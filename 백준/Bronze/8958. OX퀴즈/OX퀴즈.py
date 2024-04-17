t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    score = 0
    for i in s:
        if i == 'O':
            score +=1
            sum += score
        elif i == 'X':
            score = 0
    print(sum)