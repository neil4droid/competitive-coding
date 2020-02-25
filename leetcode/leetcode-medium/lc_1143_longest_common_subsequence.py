import unittest

class Solution(unittest.TestCase):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.longest_common_subsequence_naive(text1, text2)
        # return self.longest_common_subsequence_dp(text1, text2)
        return self.longest_common_subsequence_recursive(text1, text2)

    def longest_common_subsequence_dp(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0

        dp = [[0] * (len(text1)+1) for _ in range(0, len(text2)+1)]
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[j-1] == text2[i-1] else max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def longest_common_subsequence_recursive(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        if text1[0] == text2[0] : return 1 + self.longest_common_subsequence_recursive(text1[1:], text2[1:])
        else: return max(self.longest_common_subsequence_recursive(text1, text2[1:]), 
                            self.longest_common_subsequence_recursive(text1[1:], text2))

    def longest_common_subsequence_naive(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        
        for i in text2:
            if i in text1[k:]:
                count += 1
                k = text1.find(i)+1
        
        return count

    def test_longestCommonSubsequence(self):
        self.assertEqual(self.longestCommonSubsequence("abcde", "ace"), 3)
        ip_list = [["psnw", "vozsh"], ["oxcpqrsvwf", "shmtulqrypy"], ["bsbininm", "jmjkbkjkv"], ["abcde", "ace"], ["abc", "abc"], ["abc", "def"], ["bl", "yby"]]
        op_list = [1, 2, 1, 3, 3, 0, 1]
        for i in range(0, len(ip_list)):
            print(ip_list[i])
            self.assertEqual(self.longestCommonSubsequence(ip_list[i][0], ip_list[i][1]), op_list[i])

if __name__ == "__main__":
    unittest.main()