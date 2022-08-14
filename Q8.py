height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

from typing import List

'''
def myway(height):
    water=0
    for i in range(0, len(height)-2):
        left=height[i]
        right=height[i+2]
        if height[i]>left and height[i]>right:
            water+=1
        elif height[i]<left and height[i]<right:
            if left>right:
                water+=right-height[i]
            else:
                water+=left-height[i]
'''

#two pointer
def trap(height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

print(trap(height))