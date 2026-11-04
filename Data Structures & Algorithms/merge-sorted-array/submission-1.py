class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = [-1] * (m + n)
        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                c[k] = nums2[j]
                j += 1
                k += 1

            else:
                c[k] = nums1[i]
                i += 1
                k += 1

        while i < m:
            c[k] = nums1[i]
            k += 1
            i += 1

        while j < n:
            c[k] = nums2[j]
            j += 1
            k += 1

        for i in range(m + n):
            nums1[i] = c[i]