class Solution:
    def findMin(self, nums) -> int:
        mini = nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:  # this part is sorted, minimum is at left
                mini = min(mini, nums[left])
                right = left
            else:
                if nums[left] < nums[(left + right + 1) // 2]:  # this part is sorted
                    mini = min(mini, nums[left])
                    left = (left + right + 1) // 2
                else:
                    mini = min(mini, nums[(left + right + 1) // 2])
                    right = (left + right + 1) // 2 - 1
        return mini


s = Solution()
print(s.findMin([3, 1, 2]))
