class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        flag = False
        for i in reversed(range(len(nums) - 1)):
            if flag:
                if zero_pos - i < nums[i]:
                    flag = False
            else:
                if nums[i] == 0:
                    flag = True
                    zero_pos = i
        return not flag


s = Solution()
print(s.canJump([4,0,0,0,2,0,1]))
