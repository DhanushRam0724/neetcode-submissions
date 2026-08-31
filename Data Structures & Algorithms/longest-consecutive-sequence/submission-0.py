class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)

        maximum = 0

        for a in set1:
            if (a - 1) not in set1:
                length = 1

                while (a + length) in set1:
                    length += 1

                maximum = max(length, maximum)

        return maximum