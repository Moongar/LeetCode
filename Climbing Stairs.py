class Solution:
    def climbStairs(self, n: int) -> int:
        # first solution using bottom up dynamic programming O(n) running time
        if n == 1:
            return 1
        elif n == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, n+1):
            res = first + second
            first = second
            second = res
        return res


s = Solution()
print(s.climbStairs(4))
