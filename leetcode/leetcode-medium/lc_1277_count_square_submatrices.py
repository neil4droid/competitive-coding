import unittest
from typing import List

class Solution(unittest.TestCase):
    def countSquares(self, matrix: List[List[int]]) -> int:
        # return self.countSquares_naive(matrix)
        # return self.count_squares_dp(matrix)
        return self.count_squares_dp_2(matrix)

    def count_squares_dp(self, matrix: List[List[int]]) -> int:
        """
        Wrong answer
        """
        if not matrix: return []

        r, c = len(matrix), len(matrix[0])
        dp = []

        for i in range(0, r):
            rcount = 0
            temp_list = []
            for j in range(0, c):
                if matrix[i][j] == 1: rcount += 1
                else: rcount = 0
                temp_list.append(rcount)
            dp.append(temp_list)

        count = 0
        max_length = min(r, c)
        for i in range(0, r):
            for j in range(0, c):
                for length in range(1, max_length+1):
                    if i+length-1 >= r: 
                        break
                    if dp[i][j] >= length and dp[i+length-1][j] >= length: 
                        count += 1
                    else: 
                        break
        
        return count

    def count_squares_dp_2(self, matrix: List[List[int]]) -> int:
        """
        Method shown in: https://youtu.be/_Lf1looyJMU

        Runtime: 672 ms, faster than 70.82% of Python3 online submissions for Count Square Submatrices with All Ones.
        
        Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Count Square Submatrices with All Ones.
        """
        if not matrix: return 0
        
        r, c = len(matrix), len(matrix[0])
        dp = [[0]*(c+1) for _ in range(0, r+1)]

        count = 0
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = matrix[i-1][j-1] if matrix[i-1][j-1] == 0 else min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])+1
                count += dp[i][j]
        
        return count

    def countSquares_naive(self, matrix: List[List[int]]) -> int:
        """
        For every element in the matrix, go on checking if it forms the required submatrix, gradually increasing the length of the side of the submatrix square.

        Runtime: 1168 ms, faster than 8.67% of Python3 online submissions for Count Square Submatrices with All Ones.
        
        Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Count Square Submatrices with All Ones.
        """
        if not matrix: return 0

        count = 0
        r, c = len(matrix), len(matrix[0])
        
        for i in range(0, r):
            for j in range(0, c):
                for k in range(0, min(r, c)):
                    if i+k >= r  or j+k >= c: break
                    if self.check_submatrix(matrix, i, j, k): count += 1
                    else: break

        return count

    def check_submatrix(self, matrix, i, j, len) -> bool:
        for x in range(i, i+len+1):
            for y in range(j, j+len+1):
                if matrix[x][y] != 1: return False
        return True

    def test_countSquares(self):
        input = [
                [0,1,1,1],
                [1,1,1,1],
                [0,1,1,1]
            ]
        self.assertEqual(self.countSquares(input), 15)

        input = [
                [1,0,1],
                [1,1,0],
                [1,1,0]
            ]
        self.assertEqual(self.countSquares(input), 7)

        input = [
                [1,1,0,0,1],
                [1,0,1,1,1],
                [1,1,1,1,1],
                [1,0,1,0,1],
                [0,0,1,0,1]
                ]
        self.assertEqual(self.countSquares(input), 19)

if __name__ == "__main__":
    unittest.main()