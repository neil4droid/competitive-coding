'''
Created on 02-Dec-2019

@author: neil4droid
'''
from builtins import str
from _testmultiphase import Str

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for x in J:
            count += S.count(x)
        
        return count
    
    def num_jewels_in_stones(self, J: Str, S: str) -> int:
        return len([x for x in S if x in J])
    
    
solution = Solution()
print(solution.num_jewels_in_stones('aA', 'aAAbbbb'))