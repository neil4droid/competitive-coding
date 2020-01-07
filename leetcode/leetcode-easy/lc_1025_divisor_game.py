from typing import List
from typing import Set

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = dict()
        steps_to_one_set = self.get_steps_to_one(N, dp)
        print(N,":",steps_to_one_set)
        for i in steps_to_one_set:
            if i % 2 == 0: return False
        return True

    def get_steps_to_one(self, N: int, dp: dict) -> Set[int]:
        if dp.get(N) is not None:   return dp[N]

        steps_to_one_set = set()
        if N == 1: 
            steps_to_one_set.add(0)
            # return steps_to_one_set
        for i in range(1, N):
            if N % i == 0:
                temp_set = {x+1 for x in self.get_steps_to_one(N-i, dp)}
                steps_to_one_set = steps_to_one_set.union(temp_set)
        # return steps_to_one_set
        dp[N] = steps_to_one_set
        return steps_to_one_set

sol = Solution()
print(sol.divisorGame(2))
print(sol.divisorGame(3))
print(sol.divisorGame(4))
print(sol.divisorGame(5))
print(sol.divisorGame(6))
print(sol.divisorGame(7))
print(sol.divisorGame(8))
print(sol.divisorGame(9))