class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(i)] for i in range(1, query_row + 2)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                if dp[i][j] > 1:
                    ex = (dp[i][j] - 1) / 2
                    dp[i][j] = 1
                    dp[i+1][j] += ex
                    dp[i + 1][j + 1] += ex
        return min(dp[query_row][query_glass], 1)


s = Solution()
print(s.champagneTower(100000009, 33, 17))
