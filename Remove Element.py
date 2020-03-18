class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        count = 0
        for n in nums:
            if n != val:
                nums[count] = n
                count += 1
        return count


s = Solution()
nums = [2,3,4,3,3,1]
print(s.removeElement(nums, 3))
print(nums)