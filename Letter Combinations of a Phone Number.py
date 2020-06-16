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
        if n == 1:
            return [c for c in self.letters[digits[0]]]
        # first solution: dynamic programming
        # dp = [[] for x in range(n + 1)]
        # dp[0].append("")
        # for i in range(1, n+1):
        #     dp[i] += [y+c for y in dp[i-1] for c in self.letters[digits[i-1]]]
        # return dp[n]
        # Second solution: recursive
        return [c+y  for c in self.letters[digits[0]] for y in self.letterCombinations(digits[1:])]


s = Solution()
print(s.letterCombinations("23"))
