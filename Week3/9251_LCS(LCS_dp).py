# 최장 공통 문자열
# if i == 0 or j == 0:  # 마진 설정
# 	LCS[i][j] = 0
# elif string_A[i] == string_B[j]:
# 	LCS[i][j] = LCS[i - 1][j - 1] + 1
# else:
# 	LCS[i][j] = 0

# 최장 공통 부분 수열
# if i == 0 or j == 0:  # 마진 설정
# 	LCS[i][j] = 0
# elif string_A[i] == string_B[j]:
# 	LCS[i][j] = LCS[i - 1][j - 1] + 1
# else:
# 	LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])


s = input()
l = input()

li = [s,l ]

print(li)
li_lcs = [ [0 for _ in range(len(l) + 1)] for _ in range(len(s)+1) ] 
# * (len(s)+1)
# print(li_lcs)
result = 0
for i in range(1, len(li_lcs)):
    # print(i)
    for j in range(1, len(li_lcs[i])):
        # print(j )
        # print(s[i-1],l[j-1])
        if s[i-1] == l[j-1]:
            li_lcs[i][j] = li_lcs[i-1][j-1]+1
        else:
            li_lcs[i][j] = max(li_lcs[i-1][j],li_lcs[i][j-1])
    
    if result < max(li_lcs[i]): result = max(li_lcs[i])


# print(result)
for o in li_lcs:
    print(o)

        