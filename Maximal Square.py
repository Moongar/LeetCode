class Solution:
    def maximalSquare(self, matrix) -> int:
        # dynamic programming, O(mn) run time, O(mn) memory
        if len(matrix) == 0:
            return 0
        max_size = 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        for r in range(1, row+1):
            for c in range(1, col+1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
                    if dp[r][c] > max_size:
                        max_size = dp[r][c]
        return max_size ** 2


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
