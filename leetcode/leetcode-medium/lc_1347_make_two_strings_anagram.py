import unittest

class Solution(unittest.TestCase):
    def minSteps(self, s: str, t: str) -> int:
        # return self.minSteps_using_dict(s, t)
        return self.minSteps_naive(s, t)

    def minSteps_naive(self, s: str, t: str) -> int:
        """
        For every letter in t, if no match found in s, increment count by 1.
        If match found, delete the match from s to handle duplicates.
        Return count.

        Runtime: 1308 ms, faster than 5.12% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
        
        Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
        """
        count = 0
        for i in range(0, len(t)):
            pos = s.find(t[i])
            if pos > -1: s = s[:pos] + s[pos+1:]
            else: count += 1

        return count


    def minSteps_using_dict(self, s: str, t: str) -> int:
        """ 
        Create a dict of letter->letter-count in s string.
        For every letter in t, subtract letter count from dict.
        Return total sum of all letter counts.
        
        Runtime: 372 ms, faster than 10.49% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
        
        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
        """
        s_dict = {}

        for i in range(0, len(s)):
            s_dict[s[i]] = s_dict[s[i]] + 1 if s_dict.get(s[i]) else 1
        
        for i in range(0, len(t)):
            if s_dict.get(t[i]): s_dict[t[i]] -= 1
        
        return sum(s_dict.values())

    def test_minSteps_using_dict(self):
        self.assertEquals(self.minSteps_using_dict("bab", "bbb"), 1)
        self.assertEquals(self.minSteps_using_dict("leetcode", "practice"), 5)
        self.assertEquals(self.minSteps_using_dict("anagram", "mangaar"), 0)
        self.assertEquals(self.minSteps_using_dict("friend", "family"), 4)
    
    def test_minSteps_naive(self):
        self.assertEquals(self.minSteps_naive("bab", "bbb"), 1)
        self.assertEquals(self.minSteps_naive("leetcode", "practice"), 5)
        self.assertEquals(self.minSteps_naive("anagram", "mangaar"), 0)
        self.assertEquals(self.minSteps_naive("friend", "family"), 4)

if __name__ == "__main__":
    unittest.main()