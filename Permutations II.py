class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return [[]]
        pre = [[nums[0]]]
        perms = [[] for x in range(len(nums))]
        perms[0].append([nums[0]])
        for i in range(1, len(nums)):
            for c in perms[i-1]:
                for j in range(len(c)):
                    if c[0:j] + [nums[i]] + c[j:] not in perms[i]:
                        perms[i].append(c[0:j] + [nums[i]] + c[j:])
                if c + [nums[i]] not in perms[i]:
                    perms[i].append(c + [nums[i]])
        return perms[-1]


s = Solution()
print(s.permuteUnique([1, 2, 1]))
