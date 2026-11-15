class Solution:

    def search(self, nums, target):
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for nums in matrix:
            if nums[0] <= target <= nums[-1]:
                return self.search(nums, target)

        return False