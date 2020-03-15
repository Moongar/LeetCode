def twoSum(nums, target):
    # first solution O(n^2)
    # l = len(nums)
    # for idx1 in range(0, l - 1):
    #     res = target - nums[idx1]
    #     for idx2 in range(idx1 + 1, l):
    #         if res == nums[idx2]:
    #             return [idx1, idx2]

    # second solution O(n)
    my_dict = {}
    for idx in range(len(nums)):
        rem = target - nums[idx]
        if rem in my_dict.keys():
            return [my_dict[rem], idx]
        my_dict[nums[idx]] = idx

    return None


num_array = [9, 7, 11, 15]
target_num = 16
print(twoSum(num_array, target_num))