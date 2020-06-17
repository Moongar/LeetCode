class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return [[]]
        pre = [[nums[0]]]
        i = 1
        while i < len(nums):
            nxt = []
            for c in pre:
                for j in range(len(c)):
                    if c[0:j] + [nums[i]] + c[j:] not in nxt:
                        nxt.append(c[0:j] + [nums[i]] + c[j:])
                if c + [nums[i]] not in nxt:
                    nxt.append(c + [nums[i]])
            i += 1
            pre = nxt
        return pre


s = Solution()
print(s.permuteUnique([1, 2, 1]))
