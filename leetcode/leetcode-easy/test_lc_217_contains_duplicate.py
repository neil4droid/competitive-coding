'''
Created on 02-Dec-2019

@author: Home
'''
import unittest
from lc_217_contains_duplicate import Solution

class Test217(unittest.TestCase):
    
    solution = Solution()
    function_to_test = solution.contains_duplicates_4
    
    def test_containsDuplicate_duplicates_present(self):
        nums = [1,1,1,3,3,4,3,2,4,2,5]
        
        result = self.function_to_test(nums)
        
        self.assertIsNotNone(result)
        self.assertTrue(result)
    
    def test_containsDuplicate_duplicates_absent(self):
        nums = [1, 2, 3, 4]
        
        result = self.function_to_test(nums)
        
        self.assertIsNotNone(result)
        self.assertFalse(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()