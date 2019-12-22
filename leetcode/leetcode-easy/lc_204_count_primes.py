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
        if n <= 2: return 0
        primes_list = [1] * n
        primes_list[0] = primes_list[1] = 0
        fn_run_sieve = self.__run_sieve_over_list
        # for i in range(2, math.ceil(n/2)):  # This was the original logic I thought of
        for i in range(2, math.ceil(math.sqrt(n))):       # original, 0.201640625s average time for n upto 1500000
        # i = 2
        # while i*i < n:      # 0.210546875s average time for n upto 1500000
            if primes_list[i] == 1:
                if i>2 and i%2==0:  continue        # If no is even, do not process further. 0.201953125s average time for n upto 1500000
                primes_list = fn_run_sieve(i, n, primes_list)
            # i += 1
        return primes_list.count(1)
    
    def __run_sieve_over_list(self, number:int, n:int, input_list:List[int]) -> List[int]:
        i = number*2
        while i < n:
            input_list[i] = 0
            i += number
        return input_list

sol = Solution()
total_time_elapsed = float()
test_cases_count = 200
for _ in range(0, test_cases_count):
    random_int = random.randint(0, 1500000)
    # print("Naive:", random_int, ": ")
    # start = time.process_time()
    # print(sol.countPrimes(random_int), '   ', time.process_time() - start,'s')
    print("Sieve:", random_int, ": ")
    start = time.process_time()
    print(sol.countPrimesUsingSieve(random_int), '\n')
    time_elapsed = time.process_time() - start
    total_time_elapsed += time_elapsed
    # print("Time elapsed: ", time.process_time() - start, 's')
print('Total time elapsed: ', total_time_elapsed/test_cases_count)