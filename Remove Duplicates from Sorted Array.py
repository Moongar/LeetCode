def removeDuplicates(nums):
    # solution 1 O(n)
    # count = 0
    # my_dict = {}
    # for n in nums:
    #     if n not in my_dict.keys():
    #         my_dict[n] = 1
    #         nums[count] = n
    #         count += 1

    # second solution O(n)
    if len(nums) == 0:
        return 0
    else:
        count = 1
        current = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] > current:
                current = nums[idx]
                nums[count] = nums[idx]
                count += 1

        return count


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = []
print(removeDuplicates(nums))
print(nums)