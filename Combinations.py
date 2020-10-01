class Solution:
    def combine(self, n, k):
        combs = []
        self.backtrack(n, k, combs, [])
        return combs

    def backtrack(self, n, k, combs, path):
        if k == 0:
            combs.append(path)
            return
        for i in range(1, n+1):
            self.backtrack(n - i, k-1, combs, path + [n - i + 1])


s = Solution()
print(s.combine(4, 2))
