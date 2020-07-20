from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        oplist = []
        snums = sorted(nums)
        for i in range(0, len(snums)-2):
            if i > 0 and snums[i-1] == snums[i]: continue
            j, k = i+1, len(snums)-1
            while j < k:
                tsum = snums[i] + snums[j] + snums[k]
                if tsum == 0:
                    oplist.append([snums[i],snums[j],snums[k]])
                    while j < len(snums)-1 and snums[j+1] == snums[j]: j += 1
                    while k > j and snums[k-1] == snums[k]: k -= 1
                    j += 1
                    k -= 1
                elif tsum > 0: k -= 1
                else: j += 1
        return oplist

s = Solution()
print(s.threeSum( [0,0,0] )) # -4 -1 -1 0 1 2
print(s.threeSum( [-1,0,1,2,-1,-4] ))
print(s.threeSum( [-2,0,0,2,2] ))