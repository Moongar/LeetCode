class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        n = 1
        while n <= num:
            n = n << 1
        return (n - 1) ^ num


s = Solution()
print(s.findComplement(5))
