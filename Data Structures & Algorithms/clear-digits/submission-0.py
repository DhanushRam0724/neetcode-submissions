class Solution:
    def clearDigits(self, s: str) -> str:
        pass
        ans = []
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                ans.append(s[i])
                i += 1
            else:
                ans.pop()
                i += 1
        return "".join(ans) if len(ans) > 0 else ""