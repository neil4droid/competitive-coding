from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        desc_sorted_nums = sorted(nums, reverse=True)
        next_max_element = desc_sorted_nums[0]
        count = 0
        for i in range(1, len(nums)):
            if desc_sorted_nums[i] != next_max_element:
                next_max_element = desc_sorted_nums[i]
                count += 1
            if count == 2:
                return next_max_element
        if count < 3:
            return desc_sorted_nums[0]
    
    def third_max_without_sort(self, nums:List[int]) -> int:
        maximum = second_max = third_max = None
        maximum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maximum:
                third_max = second_max
                second_max = maximum
                maximum = nums[i]
        return third_max


sol = Solution()
nums = [3, 2, 1]
print(sol.third_max_without_sort(nums))
nums = [1, 2]
print(sol.third_max_without_sort(nums))
nums = [2, 2, 3, 1]
print(sol.third_max_without_sort(nums))