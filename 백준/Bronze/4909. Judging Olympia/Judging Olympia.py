def getAvg(li:list):
    result = 0
    for idx, i in enumerate(li):
        if idx > 0 and idx < len(li)-1:
            result += i
    # print(result)
    print(f"{result/(len(li)-2):.5f}".rstrip('0').rstrip('.'))

while True :
    nums = list(map(float, input().split()))
    
    nums.sort()

    if nums[0] == 0 and nums[len(nums)-1] == 0 :
        break
    getAvg(nums)

    