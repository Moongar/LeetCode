class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[0:-k]
        nums[0:k] = temp


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 16)
print(nums)
