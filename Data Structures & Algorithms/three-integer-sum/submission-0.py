class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            a = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] == -a and [a, nums[left], nums[right]] not in ans:
                    ans.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif [a, nums[left], nums[right]] in ans:
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < -a:
                    left += 1
                else:
                    right -= 1

        return ans