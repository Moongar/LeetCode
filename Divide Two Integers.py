class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # first solution, too slow
        if dividend == -2147483648 and divisor == -1:
            return 2 ** 31 - 1
        res = 0
        if dividend >= 0:
            if divisor > 0:
                sign = 1
            else:
                divisor = -divisor
                sign = -1
        else:
            dividend = -dividend
            if divisor > 0:
                sign = -1
            else:
                divisor = -divisor
                sign = 1
        while dividend >= divisor:
            res += 1
            dividend -= divisor
        return sign * res


s = Solution()
print(s.divide(-2**31, -1))