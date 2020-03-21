class Solution:
    def singleNumber(self, nums) -> int:
        # first solution O(n)
        open = {}
        for n in nums:
            if n in open.keys():
                open.pop(n)
            else:
                open[n] = True
        return list(open.keys())[0]


nums = [4,1,2,1,2]
s = Solution()
print(s.singleNumber(nums))