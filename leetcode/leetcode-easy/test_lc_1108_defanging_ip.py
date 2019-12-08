'''
Created on 02-Dec-2019

@author: Home
'''
import unittest
from lc_1108_defanging_ip import Solution

class Test1108(unittest.TestCase):
    def test_defangIPaddr(self):
        solution = Solution()
        defanged_ip = solution.defangIPaddr('1.2.3.4')
        
        self.assertIsNotNone(defanged_ip)
        self.assertEqual('1[.]2[.]3[.]4', defanged_ip)
        