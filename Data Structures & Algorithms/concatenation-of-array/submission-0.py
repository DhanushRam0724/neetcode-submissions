class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * (n * 2)
        for i in range(len(ans)):
            ans[i] = nums[i % n]

        return ans