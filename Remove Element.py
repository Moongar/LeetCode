class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        count = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[count] = nums[idx]
                count += 1
        return count


s = Solution()
nums = [2]
print(s.removeElement(nums, 3))
print(nums)