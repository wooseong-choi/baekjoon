n,m = map(int, input().split())
card = list(map(int, input().split()))

card.sort(reverse=True)

sum_list = set()

for i in range( len(card) ):
    for j in range( len(card) ):
        if i == j : continue
        for k in range(len(card)):
            if i == k or j == k : continue
            total = card[i]+card[j]+card[k]
            if total <= m:
                sum_list.add(total)

sum_list = sorted(sum_list, reverse=True)
print(sum_list[0])