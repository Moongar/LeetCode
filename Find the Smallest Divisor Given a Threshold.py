import math


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        div = 1
        while True:
            sum_div = sum([math.ceil(n / div) for n in nums])
            if sum_div > threshold:
                div *= 2
            else:
                break
        left = div // 2
        right = div
        while left < right:
            mid = (left + right) // 2
            if mid == right or mid == left:
                break
            sum_div = sum([math.ceil(n / mid) for n in nums])
            if sum_div > threshold:
                left = mid
            else:
                right = mid
        return right


s = Solution()
print(s.smallestDivisor([19], 5))
