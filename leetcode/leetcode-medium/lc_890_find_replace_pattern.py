import unittest
from typing import List

class Solution(unittest.TestCase):
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if not words: return []

        def match_using_dict_optimized(word: str) -> bool:
            """
            Use inner method, setdefault() function, zip() function and the filter() function to reduce the lines of code.
            The runtime for this is method is more than that of the longer version.

            Runtime: 28 ms, faster than 82.08% of Python3 online submissions for Find and Replace Pattern.
            
            Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find and Replace Pattern.
            """
            if len(word) != len(pattern): return False
            
            pattern_word_map = {}
            for k, v in zip(pattern, word):
                if pattern_word_map.setdefault(k, v) != v: 
                    return False
            return len(set(pattern_word_map.values())) == len(pattern_word_map.values())

        return filter(match_using_dict_optimized, words)
        # return [word for word in words if self.match_using_dict(word, pattern)]
    
    def match_using_dict(self, word: str, pattern: str) -> bool:
        """
        Build a map of pattern[i] -> word[i].
        
        Return false if:
            1. A different word char for a pattern char -> word char mapping already in map.
            2. A different pattern char for the same word char. This is done by comparing the length of the set of values in the map to the set of keys in the map.
        Runtime: 20 ms, faster than 98.89% of Python3 online submissions for Find and Replace Pattern.
        
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find and Replace Pattern.
        """
        if len(pattern) != len(word): return False

        pattern_word_map = {}

        for i in range(0, len(pattern)):
            if pattern_word_map.get(pattern[i]):
                if pattern_word_map[pattern[i]] != word[i]: return False
            else: pattern_word_map[pattern[i]] = word[i]
        if len(set(pattern_word_map.values())) != len(set(pattern_word_map.keys())): return False
        return True


    def test_match_using_dict_true(self):
        self.assertTrue(self.match_using_dict("mee", "abb"))
        self.assertTrue(self.match_using_dict("aqq", "abb"))
    
    def test_match_using_dict_false(self):
        self.assertFalse(self.match_using_dict("abc", "abb"))
        self.assertFalse(self.match_using_dict("dkd", "abb"))
        self.assertFalse(self.match_using_dict("ccc", "abb"))
        self.assertFalse(self.match_using_dict("gg", "ab"))
    
    def test_findAndReplacePattern(self):
        words = ["abc","deq","mee","aqq","dkd","ccc"]
        pattern = "abb"
        output = ["mee","aqq"]
        self.assertEqual(list(self.findAndReplacePattern(words, pattern)), output)

if __name__ == "__main__":
    unittest.main()