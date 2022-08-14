nums = [-1, 0, 1, 2, -1, -4]

def myway(nums: list[int])->list[list[int]]:
    results = []
    nums.sort()

    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k]==0 and [nums[i], nums[j], nums[k]] not in results:
                    results.append([nums[i], nums[j], nums[k]])
    return results

print(myway(nums))