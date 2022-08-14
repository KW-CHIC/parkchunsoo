nums = [1, 4, 3, 2]

def myway(nums:list[int])->int:
    result = 0
    nums.sort()

    for i in range(0, len(nums)):
        if i%2==0:
            result+=nums[i]
    return result

print(myway(nums))