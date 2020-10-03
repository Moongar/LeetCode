class Solution:
    def fourSum(self, nums, target):
        # second solution using three sum with two pointers
        nums.sort()
        combs = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.threeSum(nums[i + 1:], target - nums[i], nums[i], combs)
        return combs

    def threeSum(self, nums, tar, seed, combs):
        # res = []
        for idx1 in range(len(nums) - 2):
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                continue
            target = tar - nums[idx1]
            left, right = idx1 + 1, len(nums) - 1
            while right > left:
                if nums[left] + nums[right] == target:
                    combs.append([seed, nums[idx1], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return

        # first solution, backtracking, naive
    #     combs = []
    #     nums.sort()
    #     self.backtrack(nums, target, combs, [], 4)
    #     return combs
    #
    # def backtrack(self, nums, target, combs, path, k):
    #     if k == 0:
    #         if target == 0:
    #             combs.append(path)
    #         return
    #     for i in range(len(nums)):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         if len(nums) < k or target < sum(nums[0:k]):
    #             break
    #         self.backtrack(nums[i + 1:], target - nums[i], combs, path + [nums[i]], k - 1)


s = Solution()
ns = [1, 0, -1, 0, -2, 2, 2]
tar = 0
print(s.fourSum(ns, tar))
