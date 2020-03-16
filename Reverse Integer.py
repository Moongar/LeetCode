class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        while x > 0:
            rev_num = rev_num * 10 + x % 10
            x = x // 10
        rev_num *= sign
        if rev_num > 2 ** 31 - 1 or rev_num < -(2 ** 31):
            return 0
        return rev_num


s = Solution()
print(s.reverse(-1010))