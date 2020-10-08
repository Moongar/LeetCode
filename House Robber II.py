class Solution:
    def rob(self, nums) -> int:
        # bottom up dynamic programming O(n)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        val = [0 for i in range(len(nums)+1)]  # this table holds value of the best case
        val1 = [0 for i in range(len(nums)+1)]  # this table holds value of the best case without the end constraint
        val2 = [0 for i in range(len(nums) + 1)]  # this table holds value of the best case without the first house
        val1[1] = nums[0]
        val1[2] = max(nums[0], nums[1])
        val[0:3] = val1[0:3]
        val2[2] = nums[1]
        for i in range(3, len(nums)+1):
            val1[i] = max(val1[i-1], val1[i-2]+nums[i-1])
            val2[i] = max(val2[i-1], val2[i-2]+nums[i-1])
            val[i] = max(val1[i-1], val2[i])
        return val[-1]


s = Solution()
print(s.rob([1, 2, 3, 1]))
