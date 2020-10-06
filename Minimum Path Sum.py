class Solution:
    def minPathSum(self, grid) -> int:
        # first solution, bottom up dynamic programming, O(mn) running time
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        ways = [[0 for c in range(n)] for r in range(m)]
        ways[m - 1][n - 1] = grid[m-1][n-1]
        for c in range(2, n + 1):
            ways[m - 1][n - c] = ways[m - 1][n - c + 1] + grid[m - 1][n - c]
        for r in range(2, m + 1):
            ways[m-r][n-1] = ways[m-r+1][n-1] + grid[m-r][n-1]
            for c in range(2, n + 1):
                ways[m - r][n - c] = grid[m - r][n - c] + min(ways[m - r + 1][n - c], ways[m - r][n - c + 1])
        return ways[0][0]


s = Solution()
print(s.minPathSum([
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]))
