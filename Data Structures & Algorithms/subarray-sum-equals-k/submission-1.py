class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0

        freq = {0: 1}
        for i in range(len(nums)):
            total += nums[i]
            targ = total - k

            if targ in freq:
                ans += freq[targ]

            freq[total] = freq.get(total, 0 ) + 1

        return ans