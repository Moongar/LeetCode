class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        result = [False for _ in range(n+1)]
        result[1] = True
        moves = [1]
        for i in range(2, n+1):
            if i >= (moves[-1] + 1) ** 2:
                moves.append((moves[-1] + 1))
            for j in moves:
                if not result[i - j ** 2]:
                    result[i] = True
                    break
        return result[-1]


s = Solution()
print(s.winnerSquareGame(7))
