class Solution:
    def jump(self, nums) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) < 3:
            return 1
        ways = [len(nums) for i in range(len(nums))]
        ways[0:2] = [0, 1]
        for i in range(2, len(nums)):
            for j in reversed(range(i)):
                if nums[j] != 0:
                    if nums[j] >= i - j:
                        ways[i] = min(ways[i], ways[j] + 1)
        return ways[-1]


s = Solution()
print(s.jump([4, 3, 1, 1, 4]))
