import math
from typing import List
import time
import random

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        count = 1
        for i in range(3, n):
            if self.is_prime(i):
                count += 1
        return count

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        sqrt_n_plus_1 = math.ceil(math.sqrt(n))+1
        for i in range(2, sqrt_n_plus_1):
            if n % i == 0:
                return False
        return True
    
    def countPrimesUsingSieve(self, n:int) -> int:
        if n <= 2:
            return 0
        primes_list = list()
        for _ in range(0, n):
            primes_list.append(1)
        primes_list[0] = primes_list[1] = 0
        for i in range(2, math.ceil(n/2)):
            if not self.is_prime(i):
                primes_list[i] = 0
            primes_list = self.__run_sieve_over_list(i, n, primes_list)
        return primes_list.count(1)
    
    def __run_sieve_over_list(self, number:int, n:int, input_list:List[int]) -> List[int]:
        i = number + number
        while i < n:
            input_list[i] = 0
            i += number
        return input_list

sol = Solution()
for _ in range(0, 10):
    random_int = random.randint(0, 200000000)
    # print("Naive:", random_int, ": ")
    # start = time.process_time()
    # print(sol.countPrimes(random_int), '   ', time.process_time() - start,'s')
    print("Sieve:", random_int, ": ")
    start = time.process_time()
    print(sol.countPrimesUsingSieve(random_int), '  ',  time.process_time() - start,'s\n')
    # print("Time elapsed: ", time.process_time() - start, 's')
