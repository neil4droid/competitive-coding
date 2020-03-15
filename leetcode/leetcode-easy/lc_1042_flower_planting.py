from typing import List
import unittest

class Solution(unittest.TestCase):
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/flower-planting-with-no-adjacent/
        """
        return self.get_flower_arrangement(N, paths)

    def get_flower_arrangement(self, N: int, paths: List[List[int]]) -> List[int]:
        """
        Create an adjacency list. 
        For every parent node in the adj list, create a flower set = {1, 2, 3, 4}
        For every parent node in the adj list, if it does not have an already set flower, set flower to 1.
        Remove the parent node's and child nodes' flowers from the flower set.
        For the remaining children with flower = 0 or the same flower as that of the parent, pop any flower from the flower set and assign that flower to all such children.
        Continue until the second last parent node in the adj list.

        This solution does not pass the last test case below, even though the solution is correct.
        Change the nature of the test case, instead of checking of equality with a model answer array.
        """
        if not N: return []

        adj_list = self.get_adjacency_list(N, paths)
        arr = [0] * (N+1)
        for i in range(1, N):
            flowers_set = {1, 2, 3, 4}
            if arr[i] == 0: arr[i] = 1
            flowers_set.discard(arr[i])
            for child in adj_list[i]:
                flowers_set.discard(arr[child])
            flower = flowers_set.pop()
            for child in adj_list[i]:
                if arr[child] == 0 or arr[child] == arr[i]:
                    arr[child] = flower
        
        return arr[1:]

    def get_adjacency_mat(self, N: int, paths: List[List[int]]) -> List[List[int]]:
        if not N: return []

        adj = [[False] * (N+1) for _ in range(0, N+1)]
        for path in paths:
            adj[path[0]][path[1]] = True
            adj[path[1]][path[0]] = True
        for i in range(0, N+1):
            adj[i][i] = True
        
        return adj

    def get_adjacency_list(self, N: int, paths: List[List[int]]) -> List[int]:
        if not N: return []

        adj = [None] * (N+1)
        for path in paths:
            if not adj[path[0]]: adj[path[0]] = set()
            if not adj[path[1]]: adj[path[1]] = set()
            adj[path[0]].add(path[1])
            adj[path[1]].add(path[0])
        
        return adj
    
    def test_get_adjacency_mat(self):
        N = 3
        paths = [[1,2],[2,3],[3,1]]
        op = [
            [True, False, False, False],
            [False, True, True, True],
            [False, True, True, True],
            [False, True, True, True]
        ]
        self.assertEqual(self.get_adjacency_mat(N, paths), op)

    def test_get_adjacency_list(self):
        N = 3
        paths = [[1,2],[2,3],[3,1]]
        op = [None, 
            {2, 3},
            {1, 3},
            {2, 1}
        ]
        self.assertEqual(self.get_adjacency_list(N, paths), op)

    def test_gardenNoAdj(self):
        N = 3
        paths = [[1,2],[2,3],[3,1]]
        op = [1,2,3]
        self.assertEqual(self.gardenNoAdj(N, paths), op)

        N = 4
        paths = [[1,2],[3,4]]
        op = [1,2,1,2]
        self.assertEqual(self.gardenNoAdj(N, paths), op)

        N = 4
        paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
        op = [1,2,3,4]
        self.assertEqual(self.gardenNoAdj(N, paths), op)

        N = 5
        paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
        op = [1,2,1,3,3]
        self.assertEqual(self.gardenNoAdj(N, paths), op)

        N = 8
        paths = [[1,4],[1,5],[6,8],[3,5],[7,5],[3,2],[3,6],[2,7],[7,8],[1,2],[4,6]]
        op = [1,2,1,2,2,3,1,2]
        self.assertEqual(self.gardenNoAdj(N, paths), op)

if __name__ == "__main__":
    unittest.main()