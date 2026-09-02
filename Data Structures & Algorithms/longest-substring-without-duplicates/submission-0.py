class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        seen = {}

        while right < len(s):
            ch = s[right]
            if ch in seen:
                left = max(left, seen[ch])
            ans = max(ans, right - left + 1)
            seen[ch] = right + 1
            right += 1
        return ans