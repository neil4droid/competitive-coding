'''
Created on 02-Dec-2019

@author: Home
'''
from typing import List
from builtins import set

class Solution:
    def containsDuplicate(self, nums: List[int]):
        return len({n for n in nums}) < len(nums)
    
    def contains_duplicate_2(self, nums: List[int]):
        for n in nums:
            if nums.count(n) > 1:
                return True
        return False
    
    def contains_duplicates_3(self, nums: List[int]):
        return len(set(nums)) < len(nums)
    
    def contains_duplicates_4(self, nums: List[int]):
        nums.sort()
        
        for n in range(0,len(nums)):
            if n < len(nums) - 1 and nums[n] == nums[n+1]:
                return True
        
        return False
            