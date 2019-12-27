import random
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_loot = 0
        potential_targets = nums
        

sol = Solution()
input = [1,2,3,1]
print(sol.rob(input))
input = [2,7,9,3,1]
print(sol.rob(input))

for _ in range(0, 10):
    input_len = random.randint(1, 10)
    input = list()
    for i in range(0, input_len):
        input.append(random.randint(0, random.randint(0, 10)))
    print(input)