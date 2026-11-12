class Solution:
    def merge(self, nums, left, mid, right):
        i = left
        k = 0
        j = mid + 1
        c = [0] * (right - left + 1)

        while i <= mid and j <= right:
            if nums[j] < nums[i]:
                c[k] = nums[j]
                j += 1
            else:
                c[k] = nums[i]
                i += 1
            k += 1

        while i <= mid:
            c[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            c[k] = nums[j]
            k += 1
            j += 1

        for i in range(right - left + 1):
            nums[i + left] = c[i]

    def mergeSort(self, nums, low, high):
        if low < high:
            mid = (low + high) // 2

            self.mergeSort(nums, low, mid)
            self.mergeSort(nums, mid + 1, high)
            self.merge(nums, low, mid, high)

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)