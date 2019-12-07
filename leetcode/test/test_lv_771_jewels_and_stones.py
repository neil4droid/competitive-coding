'''
Created on 02-Dec-2019

@author: Home
'''
import unittest
from lc_771_jewels_and_stones import Solution

class Test771(unittest.TestCase):


    def test_numJewelsInStones(self):
        J = "aA"
        S = "aAAbbbb"
        solution = Solution()
        
        result = solution.numJewelsInStones(J, S) 
        
        self.assertIsNotNone(result)
        self.assertEqual(3, result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()