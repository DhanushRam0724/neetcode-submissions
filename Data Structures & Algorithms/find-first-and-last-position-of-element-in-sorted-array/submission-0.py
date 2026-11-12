class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1

        ans = [-1, -1]
        while start <= end:
            mid = (start + end ) // 2

            if nums[mid] == target:
                ans[0] = mid
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end ) // 2

            if nums[mid] == target:
                ans[1] = mid
                start = mid + 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return ans