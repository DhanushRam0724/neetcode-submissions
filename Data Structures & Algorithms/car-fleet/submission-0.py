class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted([(p, s) for p, s in zip(position, speed)], key=lambda t: -t[0])

        individual_time = ((target - p) / s for p, s in sorted_pos)

        fleet = 0
        lst_flt_time = 0

        for time in individual_time:
            if time > lst_flt_time:
                fleet += 1
                lst_flt_time = time


        return fleet