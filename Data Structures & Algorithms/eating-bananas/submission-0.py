import math
class Solution:
    def canEat(self, piles, hour, speed):
        h = 0
        for pile in piles:
            h += math.ceil(pile / speed)

        return h <= hour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid =  left + (right - left) // 2

            if self.canEat(piles, h, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans