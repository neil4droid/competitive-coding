import itertools
from typing import List
import unittest

class Solution(unittest.TestCase):
    def countBits(self, num: int) -> List[int]:
        return self.count_bits(num)
    
    def count_bits(self, num: int) -> List[int]:
        """
        Runtime: 1312 ms, faster than 5.00% of Python3 online submissions for Counting Bits.
        
        Memory Usage: 19.5 MB, less than 5.00% of Python3 online submissions for Counting Bits.
        """
        to_ret = []
        for i in range(0, num+1):
            to_ret.append(self.get_no_of_bits(i))
        return to_ret

    def get_no_of_bits(self, n: int) -> int:
        """
        Go on subtracting highest powers of 2 smaller than the number, and keep on incrementing the count by 1, till number reduces to 0.
        """
        if n == 0: return 0
        count = 0
        no = n
        while no:
            for i in itertools.count():
                if 2**i > no: break
            no -= 2**(i-1)
            count += 1
        
        return count
    
    def test_get_no_of_bits(self):
        self.assertEqual(self.get_no_of_bits(0), 0)
        self.assertEqual(self.get_no_of_bits(1),  1)
        self.assertEqual(self.get_no_of_bits(2),  1)
        self.assertEqual(self.get_no_of_bits(3),  2)
        self.assertEqual(self.get_no_of_bits(4),  1)
        self.assertEqual(self.get_no_of_bits(5),  2)
        self.assertEqual(self.get_no_of_bits(6),  2)
        self.assertEqual(self.get_no_of_bits(7),  3)
        self.assertEqual(self.get_no_of_bits(8),  1)
        self.assertEqual(self.get_no_of_bits(9),  2)
        self.assertEqual(self.get_no_of_bits(10),  2)
        self.assertEqual(self.get_no_of_bits(11),  3)
        self.assertEqual(self.get_no_of_bits(16),  1)

    def test_countBits(self):
        self.assertEqual(self.countBits(2), [0,1,1])
        self.assertEqual(self.countBits(5), [0,1,1,2,1,2])

if __name__ == "__main__":
    unittest.main()