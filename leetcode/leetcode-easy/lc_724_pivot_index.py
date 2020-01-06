from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        forward_sum = list()
        forward_sum.append(nums[0])
        for i in range(1, len(nums)):    
            forward_sum.append(nums[i] + forward_sum[i-1])
        for i in range(0, len(nums)):
            if i == 0:
                if forward_sum[-1] - forward_sum[0] == 0:
                    return 0
            elif i == len(nums)-1:
                if forward_sum[-2] == 0:
                    return len(nums)-1
            elif forward_sum[i-1] == forward_sum[-1] - forward_sum[i]:
                return i
        return -1


sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
print(sol.pivotIndex([1, 2, 3]))
print(sol.pivotIndex([-1,-1,-1,0,-1,-1]))
print(sol.pivotIndex([-1,-1,-1,0,1,1]))
print(sol.pivotIndex([0,-1,-1,-1,-1,-1]))