class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        leng = len(nums)
        status = False
        for value in counter.values():
            if value > 1:
                status = True
                break
        if not status:
            return False
        else:
            return True