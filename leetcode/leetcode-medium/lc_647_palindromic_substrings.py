import unittest

class Solution(unittest.TestCase):
    def countSubstrings(self, s: str) -> int:
        return self.count_palindromic_substrings_naive(s)
    
    def count_palindromic_substrings_naive(self, s: str) -> int:
        """
        For every character in the string, check is every substring starting with that character is a palindrome.
        Increase the substring length by 1.

        Time Limit Exceeded.
        """
        if not s: return 0
        count = 0
        for i in range(0, len(s)):
            if i == len(s)-1: 
                count += 1 
                continue
            for j in range(i+1, len(s)+1):
                if self.is_palindrome(s[i:j]): count += 1
        return count

    def is_palindrome(self, s: str) -> bool:
        """
        Iterative method to test if a given string is a palindrome.
        """
        if not s: return False
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

    def is_palindrome_recursive(self, s: str) -> bool:
        """
        Recursive method to test if a given string is a palindrome.
        """
        if not s: return False
        if len(s) == 1: return True
        return s[0] == s[-1] and self.is_palindrome_recursive(s[1:len(s)-1])

    def test_countSubstrings(self):
        ip, op = "abc", 3
        self.assertEqual(self.countSubstrings(ip), op)
        ip, op = "aaa", 6
        self.assertEqual(self.countSubstrings(ip), op)

    def test_is_palindrome_recursive(self):
        input = "madam"
        self.assertTrue(self.is_palindrome_recursive(input))
        self.assertTrue(self.is_palindrome(input))
        input = "aaa"
        self.assertTrue(self.is_palindrome_recursive(input))
        self.assertTrue(self.is_palindrome(input))
        input = "abc"
        self.assertFalse(self.is_palindrome_recursive(input))
        self.assertFalse(self.is_palindrome(input))

if __name__ == "__main__":
    unittest.main()