nums = [1, 2, 3, 4]

def myway(nums:list[int])->list[int]:
    result = []
    temp=1
    for i in nums:
        temp *= i

    for i in range(0, len(nums)):
        result.append(int(temp/nums[i]))

    return result

print(myway(nums))