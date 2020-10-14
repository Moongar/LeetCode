class Solution:
    def jump(self, nums) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) < 3:
            return 1
        # first solution, dynamic programming, O(n^2) time, O(n) memory
        # ways = [len(nums) for i in range(len(nums))]
        # ways[0:2] = [0, 1]
        # for i in range(2, len(nums)):
        #     for j in reversed(range(i)):
        #         if nums[j] != 0:
        #             if nums[j] >= i - j:
        #                 ways[i] = min(ways[i], ways[j] + 1)
        # return ways[-1]
        jump_count = 0
        max_jump = 0
        must_jump = 0
        for i in range(len(nums)):
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= len(nums) - 1:
                return jump_count + 1
            if i == must_jump:
                must_jump = max_jump
                jump_count += 1
        return jump_count


s = Solution()
print(s.jump([4, 3, 1, 1, 4]))
