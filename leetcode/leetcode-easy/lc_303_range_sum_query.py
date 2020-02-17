from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums_arr = nums[:]
        self.memo = self.__create_memo(nums)
        
    def __create_memo(self, nums: List[int]) -> List[int]:
        if not nums: return []

        ret_arr = []
        ret_arr.append(nums[0])
        for i in range(1, len(nums)):
            ret_arr.append(nums[i] + ret_arr[i-1])
        return ret_arr

    def sumRange(self, i: int, j: int) -> int:
        if not self.memo: return 0
        if i == 0: return self.memo[j]
        return self.memo[j] - self.memo[i-1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))