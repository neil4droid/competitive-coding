import random
from typing import List

class Solution:
    def rob_1(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        max_loot = 0
        potential_targets = list()

        for i in range(0, len(nums)):
            potential_targets[:] = nums
            max_loot_here = 0
            while potential_targets.count(-1) < len(potential_targets):
                max_loot_here += nums[i]
                potential_targets = self.update_potential_targets(potential_targets, i)
                i = potential_targets.index(max(potential_targets))
            if max_loot_here > max_loot:    max_loot = max_loot_here
        
        return max_loot
    
    def update_potential_targets(self, nums: List[int], i: int) -> List[int]:
        nums[i] = -1
        if i == 0 and len(nums) > 1:
            nums[1] = -1
        elif i == len(nums)-1 and len(nums) > 1:
            nums[-2] = -1
        elif len(nums) > 1:   nums[i-1] = nums[i+1] = -1 
        return nums
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        dp = list()
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        return dp[-1]
        
sol = Solution()
input = [1, 3, 6, 1, 1]
print(sol.rob(input))
input = [1,2,3,1]
print(sol.rob(input))

for _ in range(0, 10):
    input_len = random.randint(1, 6)
    input = list()
    for i in range(0, input_len):
        input.append(random.randint(0, random.randint(0, 10)))
    
    print(input)
    print(sol.rob(input))