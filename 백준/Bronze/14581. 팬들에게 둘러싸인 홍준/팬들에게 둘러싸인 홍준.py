n = input()
fan = ':fan:'
def printFan():
    for _ in range(3):
        print(fan, end='')
    print('\n', end='')

for i in range(3):
    if i == 1:
        print(fan+':'+n+':'+fan)
    else:
        printFan()
