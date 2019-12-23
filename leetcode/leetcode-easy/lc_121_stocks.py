import random
from typing import List

class Solution:
    def maxProfitNaive(self, prices: List[int]) -> int:
        max_profit = [None]*3
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if max_profit[0] is None or prices[j] - prices[i] > max_profit[0]:
                    max_profit = [prices[j] - prices[i], i, j]
        return max_profit if max_profit[0] is not None and max_profit[0] >= 0 else 0


print('[7,1,5,3,6,4] : ', Solution().maxProfitNaive([7,1,5,3,6,4]))
print('[7,6,4,3,1] : ', Solution().maxProfitNaive([7,6,4,3,1]))

input_count = random.randint(1, 10)
for i in range(0, input_count):
    input_length = random.randint(1, 7)
    input_list = list()
    for _ in range(0, input_length):
        input_list.append(random.randint(0, 10))
    print(input_list, ': ', Solution().maxProfitNaive(input_list))