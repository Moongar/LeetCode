def threeSum(nums):
    res = []
    nums.sort()
    for idx1 in range(len(nums)-2):
        if idx1 > 0 and nums[idx1] == nums[idx1-1]:
            continue
        target = -nums[idx1]
        # first solution, O(n^2)
        # my_dict = {}
        # pair_dict= {}
        # for idx2 in range(idx1 + 1, len(nums)):
        #     rem = target - nums[idx2]
        #     if rem in my_dict.keys():
        #         if (rem, nums[idx2]) not in pair_dict:
        #             res.append([-target, rem, nums[idx2]])
        #             pair_dict[(rem, nums[idx2])] = 1
        #     my_dict[nums[idx2]] = idx2
        # second solution with two moving pointers
        left, right = idx1 + 1, len(nums) - 1
        while right > left:
            if nums[left] + nums[right] == target:
                res.append([nums[idx1], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return res


num_array = [-1, 0, 1, 2, -1, -4]
# # num_array = [0, 0, 0, 0]
# num_array = [-2, 0, 0, 2, 2]
print(threeSum(num_array))
