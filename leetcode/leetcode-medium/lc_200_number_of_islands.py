from typing import List
import unittest

class Solution(unittest.TestCase):
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        https://leetcode.com/problems/number-of-islands/

        Create a visited matrix, init to False.
        Parse the grid. For every land bit not visited before, increment the number of islands, and mark all the surrounding land bits as visited.
        This is done recursively.

        Runtime: 128 ms, faster than 96.13% of Python3 online submissions for Number of Islands.
        
        Memory Usage: 13.8 MB, less than 62.39% of Python3 online submissions for Number of Islands.
        """
        if not grid: return 0

        islands_no = 0
        visited = [[False] * len(grid[0]) for _ in range(0, len(grid))]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    self.visit_surrounding_land(grid, visited, i, j)
                    islands_no += 1
        
        return islands_no

    def visit_surrounding_land(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int) -> List[List[bool]]:
        if not grid: return None

        if i > 0 and grid[i-1][j] == "1" and not visited[i-1][j]:
            visited[i-1][j] = True
            self.visit_surrounding_land(grid, visited, i-1, j)
        if j < len(grid[i])-1 and grid[i][j+1] == "1" and not visited[i][j+1]:
            visited[i][j+1] = True
            self.visit_surrounding_land(grid, visited, i, j+1)
        if i < len(grid)-1 and grid[i+1][j] == "1" and not visited[i+1][j]:
            visited[i+1][j] = True
            self.visit_surrounding_land(grid, visited, i+1, j)
        if j > 0 and grid[i][j-1] == "1" and not visited[i][j-1]:
            visited[i][j-1] = True
            self.visit_surrounding_land(grid, visited, i, j-1)
        
        return visited

    def test_numIslands(self):
        ip = [  ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
        op = 1
        self.assertEqual(self.numIslands(ip), op)

        ip = [  ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"], ]
        op = 3
        self.assertEqual(self.numIslands(ip), op)

if __name__ == "__main__":
    unittest.main()