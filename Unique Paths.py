class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[1 for c in range(n)] for r in range(m)]
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                ways[m - r][n - c] = ways[m - r + 1][n - c] + ways[m - r][n - c + 1]
        return ways[0][0]


s = Solution()
print(s.uniquePaths(3, 7))
