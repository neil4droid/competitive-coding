from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)
    
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Runtime: 28 ms, faster than 98.33% of Python3 online submissions for Merge Sorted Array.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
        """
        i = j = 0
        while j < n and i < m+j:
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            else: i += 1
        while j < n:
            nums1[m+j] = nums2[j]
            j += 1
        nums1 = nums1[0 : m+n]
        print(nums1)

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
sol = Solution()
sol.merge_2(nums1, m, nums2, n)