import random
from typing import List


class Solution:
    def maxProfitNaive(self, prices: List[int]) -> int:
        max_profit = [None] * 3
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if max_profit[0] is None or prices[j] - prices[i] > max_profit[0]:
                    max_profit = [prices[j] - prices[i], i, j]
        return max_profit if max_profit[0] is not None and max_profit[0] >= 0 else 0

    def max_profit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
        return max_profit


print("[7,1,5,3,6,4] : ", Solution().max_profit([7, 1, 5, 3, 6, 4]))
print("[7,6,4,3,1] : ", Solution().max_profit([7, 6, 4, 3, 1]))

input_count = random.randint(1, 10)
for i in range(0, input_count):
    input_length = random.randint(1, 7)
    input_list = list()
    for _ in range(0, input_length):
        input_list.append(random.randint(0, 10))
    print(input_list, ": ", Solution().max_profit(input_list))
