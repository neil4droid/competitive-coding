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
            if nums[i] == maximum or nums[i] == second_max or nums[i] == third_max:
                continue
            if nums[i] > maximum:
                third_max = second_max
                second_max = maximum
                maximum = nums[i]
            elif second_max is None or nums[i] > second_max:
                third_max = second_max
                second_max = nums[i]
            elif third_max is None or nums[i] > third_max:
                third_max = nums[i]
        if third_max is None:
            return maximum
        return third_max

    def third_max_without_sort_2(self, nums:List[int]) -> int:
        max_list = list()
        for i in range(0, 3+1):
            max_list.append(None)
        max_list[1] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == max_list[1] or nums[i] == max_list[2] or nums[i] == max_list[3]:
                continue
            if nums[i] > max_list[1]:
                max_list[3] = max_list[2]
                max_list[2] = max_list[1]
                max_list[1] = nums[i]
            elif max_list[2] is None or nums[i] > max_list[2]:
                max_list[3] = max_list[2]
                max_list[2] = nums[i]
            elif max_list[3] is None or nums[i] > max_list[3]:
                max_list[3] = nums[i]
        if max_list[3] is None:
            return max_list[1]
        return max_list[3]


sol = Solution()
nums = [3, 2, 1]
print(sol.third_max_without_sort_2(nums))
nums = [1, 2]
print(sol.third_max_without_sort_2(nums))
nums = [2, 2, 3, 1]
print(sol.third_max_without_sort_2(nums))
