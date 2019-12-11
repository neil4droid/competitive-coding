from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len == 0 or nums_len == 1:
            return True
        else:
            count = 0
            for i in range(0, nums_len-1):
                if nums[i+1] < nums[i]:
                    if count > 1:
                        return False
                    count += 1
                    if i == nums_len-2 or i == 0:
                        continue
                    elif nums[i+2] >= nums[i]:
                        i += 2
                    elif nums[i+2] < nums[i]:
                        if nums[i+1] < nums[i-1]:
                            count += 1
            if count <= 1:
                return True
            return False