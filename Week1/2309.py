li = []
for _ in range(9):
    li.append( int(input()) )

s = sum(li)


for iidx, i in enumerate(li) :
    for jidx,j in enumerate(li):
        if iidx != jidx:
            if 100==s - i - j:
                li.remove(j) 
                li.remove(i) 
        if len(li) == 7: break
    if len(li) == 7: break            

li.sort()
for i in li:
    print(i)
