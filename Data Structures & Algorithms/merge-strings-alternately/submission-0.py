class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) + len(word2)
        ans = [0] * n
        i = 0
        k = 0
        while k < n:
            if i < len(word1) and i < len(word2):
                ans[k] = word1[i]
                k += 1
                ans[k] = word2[i]
                i += 1
                k += 1
            
            elif i >= len(word2):
                ans[k] = word1[i]
                k += 1
                i += 1

            elif i >= len(word1):
                ans[k] = word2[i]
                i += 1
                k += 1

        return "".join(ans)