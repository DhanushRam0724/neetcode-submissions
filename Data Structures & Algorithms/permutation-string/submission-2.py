class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0 ) + 1

        k = len(s1)
        win = {}
        for i in range(k):
            win[s2[i]] = win.get(s2[i], 0) + 1
        if win == s1_dict:
            return True

        for j in range(len(s2) - k):
            win[s2[j]] -= 1
            if win[s2[j]] == 0:
                del win[s2[j]]
            win[s2[j + k]] = win.get(s2[j + k], 0 ) + 1
            if win == s1_dict:
                return True

        return False