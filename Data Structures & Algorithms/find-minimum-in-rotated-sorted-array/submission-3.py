class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float('inf')
        
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] > nums[low]:
                ans = min(ans, nums[low], nums[mid])
                low = mid + 1
            else:
                ans = min(ans, nums[mid], nums[high])
                high = mid - 1

        return ans