class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S)-1, len(T)-1
        sc1, sc2 = 0, 0
        
        while i >= 0 or j >= 0:
            while sc1 > 0:
                if i < 0: break
                if S[i] == '#': sc1 += 1
                else: sc1 -= 1
                i -= 1
            while sc2 > 0:
                if j < 0: break
                if T[j] == '#': sc2 += 1
                else: sc2 -= 1
                j -= 1
            if i >= 0 and S[i] == '#': 
                i -= 1
                sc1 += 1
                continue
            if j >= 0 and T[j] == '#': 
                j -= 1
                sc2 += 1
                continue
            if i >= 0 and j >= 0 and S[i] != T[j]: return False
            i, j = i-1, j-1
        return True

sol = Solution()
print(sol.backspaceCompare("bxo#j##tw", "bxj##tw"))