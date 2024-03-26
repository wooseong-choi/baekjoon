n, m  = map(int,input().split())
li = list(map(int,input().split()))

li.sort()
#def binary_search_evolution( list, target, total):
def binary_search_evolution( list, target, start, end):
 #   middle = total // 2
    middle = (start, end) // 2
#    cut_sum = 0

    for i in list:
        if i > middle: cut_sum += i-middle
    

    if( cut_sum == target ):
        return target
    elif cut_sum > target: return binary_search_evolution(list, target, total)
    else:  return binary_search_evolution( list, target, middle+1, total )



#def binary_search_evolution( list, target, total):
def binary_search( list, target, start, end):
 #   middle = total // 2
    middle = (start, end) // 2
#    cut_sum = 0

    for i in list:
        if i > middle: cut_sum += i-middle
    

    if( cut_sum == target ):
        return target
    elif cut_sum > target: return binary_search_evolution(list, target, total)
    else:  return binary_search_evolution( list, target, middle+1, total )

#print(sum(li))

