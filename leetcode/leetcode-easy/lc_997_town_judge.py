from typing import List
import unittest

class Solution(unittest.TestCase):
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/find-the-town-judge/
        """
        return self.find_judge(N, trust)
    
    def find_judge(self, N: int, trust: List[List[int]]) -> int:
        """
        Construct an adjacency matrix, mat[i][j] = True is i trusts j.
        For judge J, mat[anything-J][J] = True and mat[J][anything] = False

        Runtime: 860 ms, faster than 21.78% of Python3 online submissions for Find the Town Judge.

        Memory Usage: 22.6 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
        """
        if not N or not trust: return -1

        mat = [[False] * (N+1) for _ in range(0, N+1)]
        for arr in trust:
            mat[arr[0]][arr[1]] = True

        judge = -1
        for j in range(1, len(mat[0])):
            flag = True
            for i in range(1, len(mat)):
                if i != j and (not mat[i][j] or mat[j][i]):
                    flag = False
                    break
            if flag: judge = j
        
        return judge

    def test_findJudge(self):
        ip_N = 2
        ip_trust = [[1,2]]
        op = 2
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)

        ip_N = 3
        ip_trust = [[1,3],[2,3]]
        op = 3
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)
        
        ip_N = 3
        ip_trust = [[1,3],[2,3],[3,1]]
        op = -1
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)
        
        ip_N = 3
        ip_trust = [[1,2],[2,3]]
        op = -1
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)

        ip_N = 4
        ip_trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        op = 3
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)

if __name__ == "__main__":
    unittest.main()