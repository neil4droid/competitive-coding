import random
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
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

sol = Solution()
input = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
print(sol.rob(input))
input = [2,7,9,3,1]
print(sol.rob(input))

# for _ in range(0, 10):
#     input_len = random.randint(1, 10)
#     input = list()
#     for i in range(0, input_len):
#         input.append(random.randint(0, random.randint(0, 10)))
    
#     print(input)
#     print(sol.rob(input))
