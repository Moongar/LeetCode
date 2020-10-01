class Solution:
    def fourSum(self, nums, target):
        combs = []
        nums.sort()
        self.backtrack(nums, target, combs, [], 4)
        return combs

    def backtrack(self, nums, target, combs, path, k):
        if k == 0:
            if target == 0:
                combs.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[i + 1:], target - nums[i], combs, path + [nums[i]], k - 1)


s = Solution()
ns = [1, 0, -1, 0, -2, 2, 2]
tar = 0
print(s.fourSum(ns, tar))
