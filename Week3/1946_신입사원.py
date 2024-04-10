t = int(input())

import sys
for i in range(t):
    n = int(input())
    cnt =0
    lits = []
    for j in range(n):
        k, v = map(int,sys.stdin.readline().split())
        lits.append((k,v))

    lits.sort(key=lambda x: x[0])

    temp = lits[0][1]
    # print('lits == ======== === == == === ',lits)
    for j in range(n):
        # print('비교 실행',temp, lits[j][1])
        if temp >= lits[j][1]:
            # print('변경 실행 ',temp,'<==', lits[j][1])
            cnt +=1
            # print('cnt ++ ', cnt)
            temp = lits[j][1]


    print(cnt)

