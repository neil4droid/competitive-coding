'''
Created on 07-Dec-2019

@author: neil4droid
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {nums[0]: 0}
        for i in range(1, len(nums)):
            if myDict.get(target - nums[i]) is not None:
                return [myDict[target - nums[i]], i]
            else:
                myDict[nums[i]] = i             
                
sol = Solution()
print(sol.twoSum([3, 2, 4], 6))