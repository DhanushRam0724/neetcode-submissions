class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left, right = 0, len(people) - 1
        while left <= right:
            com = limit - people[right]
            right -= 1
            count += 1
            if left <= right and com >= people[left]:
                left += 1
                
            

        return count 