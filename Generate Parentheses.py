class Solution:
    def generateParenthesis(self, n: int):
        comb = [[] for i in range(n + 1)]
        comb[0].append('')
        for i in range(n + 1):
            for j in range(i):
                comb[i] += ['(' + left + ')' + right for left in comb[j] for right in comb[i - j - 1]]
        return comb[n]


s = Solution()
combs = s.generateParenthesis(4)
print(combs)