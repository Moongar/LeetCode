class Solution:
    letters = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"
               }
    def letterCombinations(self, digits: str):
        n = len(digits)
        if n == 0:
            return []
        dp = [[] for x in range(n + 1)]
        dp[0].append("")
        for i in range(1, n+1):
            dp[i] += [y+c for y in dp[i-1] for c in self.letters[digits[i-1]]]
        return dp[n]


s = Solution()
print(s.letterCombinations("29"))
m = "a"
print(m[1:])
