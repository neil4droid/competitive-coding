from typing import List

class NumArray:
    
    dp = None
    
    def __init__(self, nums: List[int]):
        if len(nums) == 0: pass
        else:
            self.dp = [0]*len(nums)
            self.dp[0] = nums[0]
            for i in range(1, len(nums)):
                self.dp[i] = nums[i] + self.dp[i-1]
            
    def sumRange(self, i: int, j: int) -> int:
        if self.dp is None: return None
        if i == 0:  return self.dp[j]
        return self.dp[j] - self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))