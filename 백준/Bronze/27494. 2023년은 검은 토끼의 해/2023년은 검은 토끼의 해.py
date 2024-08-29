n = int(input())
cnt = 0
memo = 12023
for i in range(2023, n+1):
    if len(str(i)) < 5:
        if i == 2023: cnt += 1
        else: continue
    else:
        temp_idx = 0
        strj = str(i)
        if strj.find('2') == -1: continue
        else: temp_idx = strj.find('2')
        
        if strj.find('0',temp_idx) == -1: continue
        else: temp_idx = strj.find('0',temp_idx)
        if strj.find('2',temp_idx) == -1: continue
        else: temp_idx = strj.find('2',temp_idx)
        
        if strj.find('3',temp_idx) == -1: continue
        else:
            memo = i
            cnt += 1
print(cnt)