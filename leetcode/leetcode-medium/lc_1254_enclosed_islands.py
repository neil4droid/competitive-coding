from typing import List
import unittest

class Solution(unittest.TestCase):
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-closed-islands/
        """
        return self.get_number_of_enclosed_islands(grid)
    
    def get_number_of_enclosed_islands(self, grid: List[List[int]]) -> int:
        """
        For every land bit, use DFS to visit the entire island. Change every visited land bit to water bit.
        If we visit the edge of the grid while visiting a particular island, it is not an enclosed island.

        Runtime: 144 ms, faster than 66.67% of Python3 online submissions for Number of Closed Islands.
        
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number of Closed Islands.
        """
        if not grid: return 0

        num_islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    if not self.dfs(grid, i, j): num_islands += 1
        
        return num_islands

    def dfs(self, grid: List[List[int]], i: int, j: int) -> bool:
        """
        Visit the island by marking the land bits to water bits using DFS.
        Return true if the island is NOT and enclosed island.
        Do this by checking in the dfs method if we are the edge of the grid.
        If any of the dfs methods return True, cascade that True and return it to the caller.
        """
        if not grid: return False
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]): return False
        if grid[i][j] == 1: return False

        grid[i][j] = 1
        ret_val = False
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1: ret_val = True
        dfs_up = self.dfs(grid, i-1, j)
        dfs_right = self.dfs(grid, i, j+1)
        dfs_down = self.dfs(grid, i+1, j)
        dfs_left = self.dfs(grid, i, j-1)
        
        return ret_val or dfs_up or dfs_right or dfs_down or dfs_left

    def test_dfs(self):
        ip = [  [1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
        self.assertTrue(self.dfs(ip, 0, 7))
        self.assertTrue(self.dfs(ip, 4, 7))
        self.assertFalse(self.dfs(ip, 1, 1))
        self.assertFalse(self.dfs(ip, 3, 6))

    def test_closedIsland(self):
        ip = [  [1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
        op = 2
        self.assertEqual(self.closedIsland(ip), op)
        ip = [  [0,0,1,0,0],
                [0,1,0,1,0],
                [0,1,1,1,0]]
        op = 1
        self.assertEqual(self.closedIsland(ip), op)
        ip = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
        op = 2
        self.assertEqual(self.closedIsland(ip), op)

if __name__ == "__main__":
    unittest.main()