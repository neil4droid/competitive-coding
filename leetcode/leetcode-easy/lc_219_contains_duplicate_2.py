'''
Created on 02-Dec-2019

@author: neil4droid
'''
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False
    
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        processed_list = []
        for i in range(0, len(nums)):
            try:
                if nums.index(nums[i], i+1) - i <= k:
                    return True
            except:
                pass
        return False