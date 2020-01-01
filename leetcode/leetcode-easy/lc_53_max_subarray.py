from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = list()
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[i-1]+nums[i]))
        return max(dp)