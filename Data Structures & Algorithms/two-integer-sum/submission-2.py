class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            ref = target - num
            if ref in seen:
                return [seen[ref], i]

            seen[num] = i