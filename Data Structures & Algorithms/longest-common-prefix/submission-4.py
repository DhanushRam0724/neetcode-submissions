class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = [-1] * len(strs[0])
        for i in range(len(strs[0])):
            ans[i] = strs[0][i]

        for ch in strs[1:]:
            j = 0
            x = min(len(ch), len(ans))

            if x == 0:
                return ""
            while j < x:
                if ans[j] != ch[j]:
                    i = len(ans) - j
                    y = 0
                    while y < i:
                        ans.pop()
                        y += 1
                    break
                j += 1

            if len(ch) < len(ans):
                ans = list(ch)

        return "".join(ans)