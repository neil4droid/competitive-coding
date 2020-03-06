import unittest
from typing import List

class Solution(unittest.TestCase):
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/sort-the-matrix-diagonally/
        """
        pass

    def diagonal_sort_naive(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Function to move the diagonal pointer from bottom left to top right and call sort on every diagonal.
        """
        if not mat: return None

        row_col_index = [len(mat)-1, 0]
        while row_col_index[1] < len(mat[0]):
            mat = self.sort_current_diagonal(mat, row_col_index)
            if row_col_index[0] == 0: row_col_index[1] += 1
            if row_col_index[1] == 0: row_col_index[0] -= 1
        
        return mat

    def sort_current_diagonal(self, mat: List[List[int]], row_col_index: List[int]) -> List[List[int]]:
        """
        Function to sort a diagonal using another array.
        """
        i, j = row_col_index[0], row_col_index[1]
        temp_arr = []
        while i < len(mat) and j < len(mat[0]):
            temp_arr.append(mat[i][j])
            i += 1
            j += 1
        temp_arr.sort()
        i, j = row_col_index[0], row_col_index[1]
        while i < len(mat) and j < len(mat[0]):
            mat[i][j] = temp_arr.pop(0)
            i += 1
            j += 1
        return mat

    def test_sort_current_diagonal(self):
        ip = [  [3,3,1,1],
                [2,2,1,2],
                [1,1,1,2]]
        diag = [0, 0]
        op = [[1, 3, 1, 1], [2, 2, 1, 2], [1, 1, 3, 2]]
        self.assertEqual(self.sort_current_diagonal(ip, diag), op)
    
    def test_diagonal_sort_naive(self):
        ip = [  [3,3,1,1],
                [2,2,1,2],
                [1,1,1,2]]
        op = [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
        self.assertEqual(self.diagonal_sort_naive(ip), op)

if __name__ == "__main__":
    unittest.main()