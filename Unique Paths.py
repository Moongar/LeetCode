class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # first solution, bottom up dynamic programming O(mn) running time
        # ways = [[1 for c in range(n)] for r in range(m)]
        # for r in range(2, m + 1):
        #     for c in range(2, n + 1):
        #         ways[m - r][n - c] = ways[m - r + 1][n - c] + ways[m - r][n - c + 1]
        # return ways[0][0]
        # second solution, bottom up DP, but we only keep the last two rows to reduce memory usage
        if m == 1 or n == 1:
            return 1
        ways = [[1 for c in range(n)] for r in range(2)]
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                ways[0][n - c] = ways[1][n - c] + ways[0][n - c + 1]
            ways[1] = ways[0]
        return ways[0][0]


s = Solution()
print(s.uniquePaths(3, 7))
