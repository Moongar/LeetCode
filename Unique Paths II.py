class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        ways = [[0 for c in range(n)] for r in range(m)]
        ways[m-1][n-1] = 1
        for c in range(2, n+1):
            if obstacleGrid[m-1][n-c] == 0:
                ways[m-1][n-c] = ways[m-1][n-c+1]
        for r in range(2, m + 1):
            if obstacleGrid[m-r][n-1] == 0:
                ways[m-r][n-1] = ways[m-r+1][n-1]
            for c in range(2, n + 1):
                if obstacleGrid[m - r][n - c] == 0:
                    ways[m - r][n - c] = ways[m - r + 1][n - c] + ways[m - r][n - c + 1]
        return ways[0][0]


s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
