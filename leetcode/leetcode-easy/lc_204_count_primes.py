import math

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(0, n):
            if self.__is_prime(i) is True:
                count += 1
        return count

    def __is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

sol = Solution()
print(sol.countPrimes(499979))
print(sol.countPrimes(999983))