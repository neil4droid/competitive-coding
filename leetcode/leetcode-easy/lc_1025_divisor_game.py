from typing import List
from typing import Set

# TODO: Complete the solution!

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

    def divisorGame2(self, N: int) -> bool:
        if N <= 1:  return False
        for i in range(1, N):
            if N % i == 0 and not self.divisorGame2(N-i):
                return True
        return False

    def divisorGame_dp(self, N: int) -> bool:
        dp = [False]*(N+1)
        for i in range(2, N+1):
            for j in range(1, i):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[N]

    def divisorGame_math(self, N: int) -> bool:
        return N % 2 == 0

sol = Solution()
for i in range(1, 20):
    print(i,":",sol.divisorGame_dp(i))