import math
from typing import List
import time

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        count = 0
        for i in range(3, n):
            if self.is_prime(i):
                count += 1
        return count

    def countPrimesUsingSieve(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        primes_list = list()
        for i in range(0, n):
            primes_list.append(1)
        primes_list[0] = primes_list[1] = 0
        primes_list[2] = 1
        for i in range(3, n):
            if i < n and self.is_prime(i):
                primes_list[i] = 1
                primes_list = self.cross_out_multiples(i, n, primes_list)
        
        return primes_list.count(1)
    
    def cross_out_multiples(self, prime_no: int, n: int, primes_list:List[int]) -> List[int]:
        i = prime_no
        i *= i
        while i <= n:
            primes_list[i] = 0
            i *= i
        return primes_list

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        sqrt_n_plus_1 = math.ceil(math.sqrt(n))+1
        for i in range(2, sqrt_n_plus_1):
            if n % i == 0:
                return False
        return True

sol = Solution()
start = time.process_time()
print(sol.countPrimes(499979))
print("Time elapsed: ", time.process_time() - start, 's')
start = time.process_time()
print(sol.countPrimes(999983))
print("Time elapsed: ", time.process_time() - start)