from typing import List
import unittest

class Solution(unittest.TestCase):
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/find-the-town-judge/
        """
        # return self.find_judge_adj_matrix(N, trust)
        # return self.find_judge_adj_list(N, trust)
        return self.find_judge_optimized(N, trust)
    
    def find_judge_optimized(self, N: int, trust: List[List[int]]) -> int:
        """
        Solution from: https://www.youtube.com/watch?v=2AdzmA1IC1k
        For every trust record, decrement count for trusting, increment count for trusted.
        If there is a person with count = N-1, that's the judge.
        """
        if not N: return -1

        count = [0] * (N+1)
        for t in trust:
            count[t[0]] -= 1
            count[t[1]] += 1

        return count[1:].index(N-1) + 1 if (N-1) in count else -1

    def find_judge_adj_matrix(self, N: int, trust: List[List[int]]) -> int:
        """
        Construct an adjacency matrix, mat[i][j] = True is i trusts j.
        For judge J, mat[anything-J][J] = True and mat[J][anything] = False

        Runtime: 860 ms, faster than 21.78% of Python3 online submissions for Find the Town Judge.

        Memory Usage: 22.6 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
        """
        if N == 1: return 1
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

    def find_judge_adj_list(self, N: int, trust: List[List[int]]) -> int:
        """
        Same logic as above, using an adjacency list instead of a matrix.

        Runtime: 768 ms, faster than 95.00% of Python3 online submissions for Find the Town Judge.
        
        Memory Usage: 17.2 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
        """
        if N == 1: return 1
        if not N or not trust: return -1

        adj_list = [None] * (N+1)
        for t in trust:
            if not adj_list[t[0]]: adj_list[t[0]] = [t[1]]
            else: adj_list[t[0]].append(t[1])
        
        for i in range(1, N+1):
            if not adj_list[i]:
                flag = True
                for j in range(1, N+1):
                    if i != j and (not adj_list[j] or i not in adj_list[j]): flag = False
                if flag: return i

        return -1


    def test_findJudge(self):
        ip_N = 1
        ip_trust = []
        op = 1
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)
        
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

        ip_N = 11
        ip_trust = [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
        op = -1
        self.assertEqual(self.findJudge(ip_N, ip_trust), op)

if __name__ == "__main__":
    unittest.main()