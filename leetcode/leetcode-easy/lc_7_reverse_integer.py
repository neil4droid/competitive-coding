class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if x < 0: 
            isNeg = True
            x *= -1
        
        final = 0
        while x > 0:
            final = final * 10 + (x % 10)
            x //= 10
        return final if not isNeg else -final

sol = Solution()
print(sol.reverse(123))