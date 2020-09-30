def threeSum(nums):
    res = []
    nums.sort()
    for idx1 in range(len(nums)-2):
        if idx1 > 0 and nums[idx1] == nums[idx1-1]:
            continue
        target = -nums[idx1]
        my_dict = {}
        pair_dict= {}
        for idx2 in range(idx1 + 1, len(nums)):
            rem = target - nums[idx2]
            if rem in my_dict.keys():
                if (rem, nums[idx2]) not in pair_dict:
                    res.append([-target, rem, nums[idx2]])
                    pair_dict[(rem, nums[idx2])] = 1
            my_dict[nums[idx2]] = idx2

    return res


num_array = [-1, 0, 1, 2, -1, -4]
# num_array = [0, 0, 0, 0]
# num_array = [-2, 0, 0, 2, 2]
print(threeSum(num_array))
