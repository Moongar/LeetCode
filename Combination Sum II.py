class Solution:
    def combinationSum2(self, candidates, target):
        combs = []
        candidates.sort()
        self.backtrack(candidates, target, combs, [])
        return combs

    def backtrack(self, candidates, target, combs, path):
        if target == 0:
            combs.append(path)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            else:
                self.backtrack(candidates[i + 1:], target - candidates[i], combs, path + [candidates[i]])


s = Solution()
cands = [10, 1, 2, 7, 6, 1, 5, 1]
tar = 8
print(s.combinationSum2(cands, tar))
