class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        pre = [[nums[0]]]
        i = 1
        while i < len(nums):
            nxt = [c[0:j]+[nums[i]]+c[j:] for c in pre for j in range(len(c) + 1)]
            pre = nxt
            i += 1
        return pre
        # perms = [[] for x in range(len(nums))]
        # perms[0].append([nums[0]])
        # for i in range(1, len(nums)):
            # second solution
            # perms[i] = [c[0:j]+[nums[i]]+c[j:] for c in perms[i-1] for j in range(len(c) + 1)]
            #first solution
            # for c in perms[i-1]:
            #     for j in range(len(c)):
            #         perms[i].append(c[0:j]+[nums[i]]+c[j:])
            #     perms[i].append(c+[nums[i]])
        # return perms[-1]


s= Solution()
print(s.permute([1, 2, 3]))
