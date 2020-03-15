def twoSum(nums, target):
    l = len(nums)
    for idx1 in range(0, l - 1):
        res = target - nums[idx1]
        for idx2 in range(idx1 + 1, l):
            if res == nums[idx2]:
                return [idx1, idx2]

    return None


num_array = [9, 7, 11, 15]
target_num = 18
print(twoSum(num_array, target_num))