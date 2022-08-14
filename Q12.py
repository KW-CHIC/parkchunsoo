nums = [7, 1, 5, 3, 6, 4]

def myway(nums:list[int])->int:
    result = 0
    low = nums[0]

    for i in range(1, len(nums)):
        low = min(low, nums[i])
        result = max(result, nums[i]-low)

    return result

print(myway(nums))