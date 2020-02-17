from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        self.cost = cost
        self.top_down_memo = [0, 0] + [None] * (len(cost)-1)
        return self.get_min_cost_to_position(len(cost))

    def get_min_cost_to_position(self, position: int) -> int:
        if self.top_down_memo[position] is not None: return self.top_down_memo[position] 
        self.top_down_memo[position] = min(self.get_min_cost_to_position(position-1) + self.cost[position-1], 
                                    self.get_min_cost_to_position(position-2) + self.cost[position-2])
        return self.top_down_memo[position]
    
    def get_min_cost_using_bottom_up_memo(self, cost: List[int]) -> int:
        if not cost: return 0
        memo = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
        
        return memo[-1]


sol = Solution()
input_cost = [10, 15, 20]
print(sol.get_min_cost_using_bottom_up_memo(input_cost))
input_cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(sol.get_min_cost_using_bottom_up_memo(input_cost))