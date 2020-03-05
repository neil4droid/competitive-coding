from typing import List
import unittest

class Solution(unittest.TestCase):
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        pass
    
    def min_fall_dp(self, mat: List[List[int]]) -> int:
        dp = [[0] * len(mat[0]) for _ in range(0, len(mat))]
        dp[0] = mat[0][:]

        for i in range(1, len(mat)):
            for j in range(0, len(mat[0])):
                if j == 0:
                    dp[i][j] = mat[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == len(mat[0])-1:
                    dp[i][j] = mat[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = mat[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
        
        return min(dp[-1])

sol = Solution()
ip =    [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]]
print(sol.min_fall_dp(ip))
