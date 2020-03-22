class Solution:
    @staticmethod
    def calc_vol(nums, left, right):
        vol = 0
        max_level = min(nums[left], nums[right])
        for idx in range(left + 1, right):
            vol += max_level - nums[idx]
        return vol

    def trap(self, height) -> int:
        if len(height) < 3:
            return 0
        total = 0
        left = 0
        for idx in range(1, len(height)):
            if height[idx] >= height[left]:
                if idx == left + 1:
                    # move the left side
                    left = idx
                else:
                    pass


        return total


numbers = [0,1,0,2,1,0,1,3,2,1,2,1]
s= Solution()
print(s.calc_vol(numbers, 3, 7))
print(s.trap(numbers))