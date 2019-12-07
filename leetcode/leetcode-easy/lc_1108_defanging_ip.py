'''
Created on 02-Dec-2019

@author: neil4droid
'''

class Solution:
    def defangIPaddr(self, address: str) -> str :
        return address.replace('.', '[.]')

solution = Solution()
print(solution.defangIPaddr('1.2.3.4'))