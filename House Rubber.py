class Solution:
    def rob(self, nums) -> int:
        # bottom up dynamic programming O(n)
        if len(nums) == 0:
            return 0
        val = [0 for i in range(len(nums)+1)]
        val[1] = nums[0]
        for i in range(2, len(nums)+1):
            val[i] = max(val[i-1], val[i-2]+nums[i-1])
        return val[-1]


s = Solution()
print(s.rob([2, 1, 1, 2]))
