from typing import List
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(unittest.TestCase):
    def maxLevelSum(self, root: TreeNode) -> int:
        return self.max_level_sum(root)

    def max_level_sum(self, root: TreeNode) -> int:
        pass
    
    def dfs(self, root: TreeNode) -> List[int]:
        if not root: return []

        arr = [root.val]
        arr += self.dfs(root.left)
        arr += self.dfs(root.right)

        return arr

    def create_tree(self, val_list: List[int], root_index: int) -> TreeNode:
        if not val_list: return None
        if root_index >= len(val_list): return None

        node = TreeNode(val_list[root_index])
        node.left = self.create_tree(val_list, 2*root_index + 1)
        node.right = self.create_tree(val_list, 2*root_index + 2)

        return node
    
    def test_dfs(self):
        ip = [1,7,0,7,-8,None,None]
        t0 = TreeNode(ip[0])
        t1 = TreeNode(ip[1])
        t2 = TreeNode(ip[2])
        t3 = TreeNode(ip[3])
        t4 = TreeNode(ip[4])
        t5 = TreeNode(ip[5])
        t6 = TreeNode(ip[6])
        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        op = [1, 7, 7, -8, 0, None, None]
        self.assertEqual(self.dfs(t0), op)

    def test_create_tree(self):
        ip = [1,7,0,7,-8,None,None]
        op = [1, 7, 7, -8, 0, None, None]
        self.assertEqual(self.dfs(self.create_tree(ip, 0)), op)

    def test_maxLevelSum(self) -> TreeNode:
        ip = [1,7,0,7,-8,None,None]
        root = self.create_tree(ip, 0)
        op = 2
        self.assertEqual(self.maxLevelSum(root), op)

if __name__ == "__main__":
    unittest.main()