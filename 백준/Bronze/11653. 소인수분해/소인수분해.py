num = int(input())

i = 2
while(1):
    if(num % i ==0):
        num = num / i
        print(i)
        continue
    i+=1

    if(num == 1):
        break    