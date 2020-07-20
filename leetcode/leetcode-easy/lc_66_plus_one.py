from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0: break
        
        if digits[0] == 0: digits.insert(0, 1)
        return digits

sol = Solution()
print(sol.plusOne([9]))