class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climb_stairs_memoized(self, n: int) -> int:
        if n <= 2: return n

        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]