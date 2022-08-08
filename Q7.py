nums = [2, 7, 11, 15]
target = int(9)

import time

def myway(nums, target):
    for i in range(0, len(nums)-1):
        if nums[i]>target: #nums가 모두 양수라 가정
            del nums[i]
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)):
            if nums[i]+nums[j]==target:
                print([i, j])
                return

#start=time.perf_counter()
myway(nums, target)
#end = time.perf_counter()
#print("\n시간", round((end - start) * 1000))