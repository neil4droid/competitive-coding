from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        mySet = set()
        for i in range(1, len(nums)):
            num_slice = nums[slice(i)]
            if nums[i] < max(num_slice):
                mySet.add(i)
            if len(mySet) > 1:
                return False
        if len(mySet) <= 1:
            return True