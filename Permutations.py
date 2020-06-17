class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        perms = [[] for x in range(len(nums))]
        perms[0].append([nums[0]])
        for i in range(1, len(nums)):
            for c in perms[i-1]:
                for j in range(len(c)):
                    perms[i].append(c[0:j]+[nums[i]]+c[j:])
                perms[i].append(c+[nums[i]])
        return perms[-1]


s= Solution()
print(s.permute([1, 2, 3]))
