def threeSumClosest(nums, target):
    nums.sort()
    closest = sum(nums[0:3])
    if closest == target:
        return target
    elif closest > target:
        return closest
    for f in range(len(nums)-2):
        rem = target - nums[f]
        left, right = f + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == rem:
                return target
            elif nums[left] + nums[right] < rem:
                if rem - nums[left] - nums[right] < abs(closest - target):
                    closest = nums[f] + nums[left] + nums[right]
                left += 1
            else:
                if -rem + nums[left] + nums[right] < abs(closest - target):
                    closest = nums[f] + nums[left] + nums[right]
                right -= 1
    return closest


nums_list = [-1, 2, 1, -4]
target_num = 1
print(threeSumClosest(nums_list, target_num))
