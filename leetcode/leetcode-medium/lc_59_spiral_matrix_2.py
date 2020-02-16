from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[False for _ in range(n)] for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r, c, di = 0, 0, 0

        for num in range(1, n*n + 1):
            ans[r][c] = num
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and not ans[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        return ans


sol = Solution()
print(sol.generateMatrix(1))
print(sol.generateMatrix(2))
print(sol.generateMatrix(3))
print(sol.generateMatrix(4))