class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c, d in zip(s, t):
            if c in s_dict and s_dict[c] != d:
                return False

            if d in t_dict and t_dict[d] != c:
                return False

            s_dict[c] = d
            t_dict[d] = c

        return True