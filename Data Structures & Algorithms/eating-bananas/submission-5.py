import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        min_valid_speed = right

        while left <= right:
            speed = (left + right) // 2
            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile / speed)

            if hours_needed <= h:
                min_valid_speed = min(min_valid_speed, speed)
                right = speed - 1  # Try a slower speed
            else:
                left = speed + 1   # Need a faster speed

        return min_valid_speed