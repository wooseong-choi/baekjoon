a = input()
b = input()

result = ''
for i in range(len(a)):
    result += a[i]+b[i]

# print(result)

def goonghap(hamnum):
    
    if len(hamnum) == 2:
        return print(hamnum)

    returnstring = ''
    for i in range(1,len(hamnum)):        
        returnstring += str(int(hamnum[i-1])+int(hamnum[i]))[-1]    
    goonghap(returnstring)

goonghap(result)
